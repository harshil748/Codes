"""
Assignment 5: Write a program to end-to-end pre-process the image:
Noise filter >>> Contrast Enhancement >>> Image Sharpening >>> Object Detection >>> ROI segmentation.
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter, ImageEnhance
import cv2
from scipy import ndimage
from scipy.ndimage import gaussian_filter, median_filter
from skimage import filters, segmentation, measure, morphology
from skimage.feature import peak_local_max, blob_dog, blob_log, blob_doh
from skimage.segmentation import watershed, active_contour
from skimage.measure import label, regionprops
import warnings

warnings.filterwarnings("ignore")

# ==================== NOISE FILTERING ====================


class NoiseFilter:
    """Various noise filtering techniques"""

    @staticmethod
    def gaussian_filter(image, sigma=1.0):
        """Apply Gaussian filter for noise reduction"""
        if len(image.shape) == 3:
            # Color image
            filtered = np.zeros_like(image)
            for i in range(image.shape[2]):
                filtered[:, :, i] = ndimage.gaussian_filter(image[:, :, i], sigma=sigma)
            return filtered
        else:
            # Grayscale image
            return ndimage.gaussian_filter(image, sigma=sigma)

    @staticmethod
    def median_filter(image, size=3):
        """Apply median filter for salt-and-pepper noise"""
        if len(image.shape) == 3:
            # Color image
            filtered = np.zeros_like(image)
            for i in range(image.shape[2]):
                filtered[:, :, i] = ndimage.median_filter(image[:, :, i], size=size)
            return filtered
        else:
            # Grayscale image
            return ndimage.median_filter(image, size=size)

    @staticmethod
    def bilateral_filter(image, d=9, sigma_color=75, sigma_space=75):
        """Apply bilateral filter (preserves edges while reducing noise)"""
        if len(image.shape) == 3:
            return cv2.bilateralFilter(image, d, sigma_color, sigma_space)
        else:
            return cv2.bilateralFilter(image, d, sigma_color, sigma_space)

    @staticmethod
    def morphological_filter(image, operation="opening", kernel_size=3):
        """Apply morphological filtering"""
        kernel = np.ones((kernel_size, kernel_size), np.uint8)

        if operation == "opening":
            return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
        elif operation == "closing":
            return cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
        elif operation == "erosion":
            return cv2.erode(image, kernel, iterations=1)
        elif operation == "dilation":
            return cv2.dilate(image, kernel, iterations=1)
        else:
            return image

    @staticmethod
    def wiener_filter(image, noise_variance=0.01):
        """Simple Wiener filter implementation"""
        # Convert to frequency domain
        f_transform = np.fft.fft2(image)
        f_shift = np.fft.fftshift(f_transform)

        # Estimate power spectral density
        magnitude = np.abs(f_shift)
        power_spectrum = magnitude**2

        # Wiener filter
        wiener_filter = power_spectrum / (power_spectrum + noise_variance)

        # Apply filter
        filtered_shift = f_shift * wiener_filter
        filtered_transform = np.fft.ifftshift(filtered_shift)
        filtered_image = np.fft.ifft2(filtered_transform)

        return np.real(filtered_image)


# ==================== CONTRAST ENHANCEMENT ====================


class ContrastEnhancement:
    """Various contrast enhancement techniques"""

    @staticmethod
    def histogram_equalization(image):
        """Apply histogram equalization"""
        if len(image.shape) == 3:
            # Color image - apply to each channel
            enhanced = np.zeros_like(image)
            for i in range(image.shape[2]):
                enhanced[:, :, i] = cv2.equalizeHist(image[:, :, i])
            return enhanced
        else:
            # Grayscale image
            return cv2.equalizeHist(image)

    @staticmethod
    def adaptive_histogram_equalization(image, clip_limit=2.0, tile_grid_size=(8, 8)):
        """Apply Contrast Limited Adaptive Histogram Equalization (CLAHE)"""
        clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)

        if len(image.shape) == 3:
            # Color image - convert to LAB and apply to L channel
            lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
            lab[:, :, 0] = clahe.apply(lab[:, :, 0])
            return cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
        else:
            # Grayscale image
            return clahe.apply(image)

    @staticmethod
    def gamma_correction(image, gamma=1.0):
        """Apply gamma correction"""
        # Normalize to [0, 1]
        normalized = image.astype(np.float32) / 255.0
        # Apply gamma correction
        corrected = np.power(normalized, gamma)
        # Convert back to [0, 255]
        return (corrected * 255).astype(np.uint8)

    @staticmethod
    def linear_stretch(image, low_percentile=2, high_percentile=98):
        """Apply linear contrast stretching"""
        if len(image.shape) == 3:
            enhanced = np.zeros_like(image)
            for i in range(image.shape[2]):
                channel = image[:, :, i]
                p_low = np.percentile(channel, low_percentile)
                p_high = np.percentile(channel, high_percentile)
                enhanced[:, :, i] = np.clip(
                    (channel - p_low) * 255 / (p_high - p_low), 0, 255
                )
            return enhanced.astype(np.uint8)
        else:
            p_low = np.percentile(image, low_percentile)
            p_high = np.percentile(image, high_percentile)
            return np.clip((image - p_low) * 255 / (p_high - p_low), 0, 255).astype(
                np.uint8
            )

    @staticmethod
    def adaptive_gamma_correction(image):
        """Adaptive gamma correction based on image statistics"""
        if len(image.shape) == 3:
            # Convert to grayscale for statistics
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image

        # Calculate mean intensity
        mean_intensity = np.mean(gray) / 255.0

        # Adaptive gamma calculation
        if mean_intensity < 0.5:
            gamma = 0.5 + (0.5 - mean_intensity)
        else:
            gamma = 0.5 + (mean_intensity - 0.5) * 0.5

        return ContrastEnhancement.gamma_correction(image, gamma)


# ==================== IMAGE SHARPENING ====================


class ImageSharpening:
    """Various image sharpening techniques"""

    @staticmethod
    def unsharp_masking(image, sigma=1.0, strength=1.5):
        """Apply unsharp masking for image sharpening"""
        if len(image.shape) == 3:
            sharpened = np.zeros_like(image, dtype=np.float32)
            for i in range(image.shape[2]):
                channel = image[:, :, i].astype(np.float32)
                blurred = gaussian_filter(channel, sigma=sigma)
                mask = channel - blurred
                sharpened[:, :, i] = channel + strength * mask
            return np.clip(sharpened, 0, 255).astype(np.uint8)
        else:
            image_float = image.astype(np.float32)
            blurred = gaussian_filter(image_float, sigma=sigma)
            mask = image_float - blurred
            sharpened = image_float + strength * mask
            return np.clip(sharpened, 0, 255).astype(np.uint8)

    @staticmethod
    def laplacian_sharpening(image, strength=1.0):
        """Apply Laplacian sharpening"""
        # Laplacian kernel
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

        if len(image.shape) == 3:
            sharpened = np.zeros_like(image)
            for i in range(image.shape[2]):
                sharpened[:, :, i] = cv2.filter2D(image[:, :, i], -1, kernel * strength)
            return sharpened
        else:
            return cv2.filter2D(image, -1, kernel * strength)

    @staticmethod
    def high_pass_filter(image, cutoff_frequency=0.1):
        """Apply high-pass filter for sharpening"""
        # Create high-pass filter in frequency domain
        rows, cols = image.shape[:2]
        crow, ccol = rows // 2, cols // 2

        # Create mask
        mask = np.ones((rows, cols), np.uint8)
        r = int(cutoff_frequency * min(rows, cols))
        center = [crow, ccol]
        x, y = np.ogrid[:rows, :cols]
        mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r * r
        mask[mask_area] = 0

        if len(image.shape) == 3:
            sharpened = np.zeros_like(image)
            for i in range(image.shape[2]):
                f_transform = np.fft.fft2(image[:, :, i])
                f_shift = np.fft.fftshift(f_transform)
                f_shift_filtered = f_shift * mask
                f_ishift = np.fft.ifftshift(f_shift_filtered)
                filtered = np.fft.ifft2(f_ishift)
                sharpened[:, :, i] = np.abs(filtered)
            return sharpened.astype(np.uint8)
        else:
            f_transform = np.fft.fft2(image)
            f_shift = np.fft.fftshift(f_transform)
            f_shift_filtered = f_shift * mask
            f_ishift = np.fft.ifftshift(f_shift_filtered)
            filtered = np.fft.ifft2(f_ishift)
            return np.abs(filtered).astype(np.uint8)


# ==================== OBJECT DETECTION ====================


class ObjectDetection:
    """Various object detection techniques"""

    @staticmethod
    def edge_detection(image, method="canny", **kwargs):
        """Apply edge detection"""
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image

        if method == "canny":
            low_threshold = kwargs.get("low_threshold", 50)
            high_threshold = kwargs.get("high_threshold", 150)
            return cv2.Canny(gray, low_threshold, high_threshold)
        elif method == "sobel":
            sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
            sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
            return np.sqrt(sobelx**2 + sobely**2)
        elif method == "laplacian":
            return cv2.Laplacian(gray, cv2.CV_64F)
        else:
            return gray

    @staticmethod
    def blob_detection(image, method="log", **kwargs):
        """Detect blobs in image"""
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image

        gray_normalized = gray / 255.0

        if method == "log":
            blobs = blob_log(gray_normalized, max_sigma=30, num_sigma=10, threshold=0.1)
        elif method == "dog":
            blobs = blob_dog(gray_normalized, max_sigma=30, threshold=0.1)
        elif method == "doh":
            blobs = blob_doh(gray_normalized, max_sigma=30, threshold=0.01)
        else:
            blobs = blob_log(gray_normalized, max_sigma=30, num_sigma=10, threshold=0.1)

        # Convert sigma to radius
        blobs[:, 2] = blobs[:, 2] * np.sqrt(2)
        return blobs

    @staticmethod
    def contour_detection(image, min_area=100):
        """Detect contours in image"""
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image

        # Apply threshold
        _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

        # Find contours
        contours, _ = cv2.findContours(
            binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        # Filter by area
        filtered_contours = [c for c in contours if cv2.contourArea(c) > min_area]

        return filtered_contours

    @staticmethod
    def corner_detection(image, method="harris", **kwargs):
        """Detect corners in image"""
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image

        gray = np.float32(gray)

        if method == "harris":
            dst = cv2.cornerHarris(gray, 2, 3, 0.04)
            corners = np.where(dst > 0.01 * dst.max())
            return list(zip(corners[1], corners[0]))  # (x, y) format
        elif method == "shi_tomasi":
            corners = cv2.goodFeaturesToTrack(gray.astype(np.uint8), 25, 0.01, 10)
            if corners is not None:
                return [(int(x), int(y)) for [[x, y]] in corners]
            else:
                return []
        else:
            return []


# ==================== ROI SEGMENTATION ====================


class ROISegmentation:
    """Region of Interest segmentation techniques"""

    @staticmethod
    def threshold_segmentation(image, method="otsu"):
        """Apply threshold-based segmentation"""
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image

        if method == "otsu":
            _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        elif method == "adaptive":
            binary = cv2.adaptiveThreshold(
                gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
            )
        else:
            _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

        return binary

    @staticmethod
    def watershed_segmentation(image, markers=None):
        """Apply watershed segmentation"""
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image

        # Generate markers if not provided
        if markers is None:
            # Noise removal
            kernel = np.ones((3, 3), np.uint8)
            opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel, iterations=2)

            # Sure background area
            sure_bg = cv2.dilate(opening, kernel, iterations=3)

            # Sure foreground area
            dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
            _, sure_fg = cv2.threshold(
                dist_transform, 0.7 * dist_transform.max(), 255, 0
            )

            # Unknown region
            sure_fg = np.uint8(sure_fg)
            unknown = cv2.subtract(sure_bg, sure_fg)

            # Marker labelling
            _, markers = cv2.connectedComponents(sure_fg)
            markers = markers + 1
            markers[unknown == 255] = 0

        # Apply watershed
        if len(image.shape) == 3:
            segmented = cv2.watershed(image, markers)
        else:
            # Convert grayscale to color for watershed
            image_color = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
            segmented = cv2.watershed(image_color, markers)

        return segmented

    @staticmethod
    def region_growing(image, seed_points, threshold=10):
        """Apply region growing segmentation"""
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image

        rows, cols = gray.shape
        segmented = np.zeros_like(gray)

        for seed_x, seed_y in seed_points:
            if segmented[seed_y, seed_x] != 0:
                continue

            # Region growing from seed point
            stack = [(seed_x, seed_y)]
            region_value = 255
            seed_intensity = gray[seed_y, seed_x]

            while stack:
                x, y = stack.pop()

                if x < 0 or x >= cols or y < 0 or y >= rows or segmented[y, x] != 0:
                    continue

                if abs(int(gray[y, x]) - int(seed_intensity)) <= threshold:
                    segmented[y, x] = region_value

                    # Add neighbors
                    stack.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])

        return segmented

    @staticmethod
    def kmeans_segmentation(image, k=3):
        """Apply K-means segmentation"""
        if len(image.shape) == 3:
            data = image.reshape((-1, 3))
        else:
            data = image.reshape((-1, 1))

        data = np.float32(data)

        # Define criteria and apply kmeans
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        _, labels, centers = cv2.kmeans(
            data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS
        )

        # Convert back to image format
        centers = np.uint8(centers)
        segmented_data = centers[labels.flatten()]
        segmented_image = segmented_data.reshape(image.shape)

        return segmented_image, labels.reshape(image.shape[:2])


# ==================== IMAGE PROCESSING PIPELINE ====================


class ImageProcessingPipeline:
    """Complete end-to-end image processing pipeline"""

    def __init__(self):
        self.steps = []
        self.results = {}

    def add_step(self, step_name, function, **kwargs):
        """Add a processing step to the pipeline"""
        self.steps.append({"name": step_name, "function": function, "kwargs": kwargs})

    def process(self, image, save_intermediate=True):
        """Process image through the entire pipeline"""
        current_image = image.copy()
        self.results = {"original": image.copy()}

        print("Starting image processing pipeline...")
        print(f"Original image shape: {image.shape}")

        for i, step in enumerate(self.steps):
            print(f"\nStep {i+1}: {step['name']}")

            try:
                processed_image = step["function"](current_image, **step["kwargs"])

                if save_intermediate:
                    self.results[step["name"]] = processed_image.copy()

                current_image = processed_image
                print(f"✓ {step['name']} completed")

            except Exception as e:
                print(f"✗ Error in {step['name']}: {e}")
                continue

        self.results["final"] = current_image
        print(f"\nPipeline completed. Final image shape: {current_image.shape}")
        return current_image

    def visualize_results(self, save_path=None):
        """Visualize all processing steps"""
        n_results = len(self.results)
        cols = 3
        rows = (n_results + cols - 1) // cols

        fig, axes = plt.subplots(rows, cols, figsize=(15, 5 * rows))
        if rows == 1:
            axes = axes.reshape(1, -1)

        for i, (name, image) in enumerate(self.results.items()):
            row = i // cols
            col = i % cols

            ax = axes[row, col]

            if len(image.shape) == 3:
                ax.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            else:
                ax.imshow(image, cmap="gray")

            ax.set_title(name.replace("_", " ").title())
            ax.axis("off")

        # Hide unused subplots
        for i in range(n_results, rows * cols):
            row = i // cols
            col = i % cols
            axes[row, col].axis("off")

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches="tight")

        plt.show()
        return fig


# ==================== SAMPLE IMAGE GENERATION ====================


def create_sample_image():
    """Create a sample image for testing the pipeline"""
    # Create a synthetic image with various features
    img = np.zeros((300, 400, 3), dtype=np.uint8)

    # Background
    img[:, :] = (50, 50, 100)

    # Add some geometric shapes
    cv2.circle(img, (100, 100), 40, (255, 255, 255), -1)  # White circle
    cv2.rectangle(img, (200, 50), (350, 150), (255, 0, 0), -1)  # Blue rectangle
    cv2.ellipse(img, (150, 200), (60, 30), 45, 0, 360, (0, 255, 0), -1)  # Green ellipse

    # Add some noise
    noise = np.random.normal(0, 25, img.shape).astype(np.int16)
    img = np.clip(img.astype(np.int16) + noise, 0, 255).astype(np.uint8)

    # Add some lines
    cv2.line(img, (0, 250), (400, 250), (255, 255, 0), 3)
    cv2.line(img, (50, 0), (50, 300), (255, 0, 255), 2)

    return img


# ==================== MAIN DEMONSTRATION ====================


def demonstrate_pipeline():
    """Demonstrate the complete image processing pipeline"""
    print("Assignment 5: End-to-End Image Processing Pipeline")
    print("=" * 60)

    # Create sample image
    sample_image = create_sample_image()

    # Create pipeline
    pipeline = ImageProcessingPipeline()

    # Step 1: Noise Filtering
    pipeline.add_step(
        "noise_filtering",
        NoiseFilter.bilateral_filter,
        d=9,
        sigma_color=75,
        sigma_space=75,
    )

    # Step 2: Contrast Enhancement
    pipeline.add_step(
        "contrast_enhancement",
        ContrastEnhancement.adaptive_histogram_equalization,
        clip_limit=3.0,
        tile_grid_size=(8, 8),
    )

    # Step 3: Image Sharpening
    pipeline.add_step(
        "image_sharpening", ImageSharpening.unsharp_masking, sigma=1.0, strength=1.5
    )

    # Step 4: Object Detection (Edge Detection)
    pipeline.add_step(
        "edge_detection",
        ObjectDetection.edge_detection,
        method="canny",
        low_threshold=50,
        high_threshold=150,
    )

    # Process through pipeline
    final_result = pipeline.process(sample_image)

    # Visualize results
    pipeline.visualize_results(
        "/Users/harshilpatel/CODE/Major/assignment_05_pipeline_results.png"
    )

    # Additional object detection demonstrations
    print("\n=== Additional Object Detection ===")

    # Blob detection
    blobs = ObjectDetection.blob_detection(sample_image, method="log")
    print(f"Detected {len(blobs)} blobs")

    # Corner detection
    corners = ObjectDetection.corner_detection(sample_image, method="harris")
    print(f"Detected {len(corners)} corners")

    # Contour detection
    contours = ObjectDetection.contour_detection(sample_image, min_area=500)
    print(f"Detected {len(contours)} contours")

    # ROI Segmentation demonstrations
    print("\n=== ROI Segmentation ===")

    # Threshold segmentation
    thresh_seg = ROISegmentation.threshold_segmentation(sample_image, method="otsu")
    print("Threshold segmentation completed")

    # K-means segmentation
    kmeans_seg, labels = ROISegmentation.kmeans_segmentation(sample_image, k=4)
    print("K-means segmentation completed")

    # Watershed segmentation
    watershed_seg = ROISegmentation.watershed_segmentation(sample_image)
    print("Watershed segmentation completed")

    # Create comprehensive visualization
    fig, axes = plt.subplots(3, 3, figsize=(15, 15))

    # Row 1: Original processing steps
    axes[0, 0].imshow(cv2.cvtColor(sample_image, cv2.COLOR_BGR2RGB))
    axes[0, 0].set_title("Original Image")
    axes[0, 0].axis("off")

    axes[0, 1].imshow(
        cv2.cvtColor(pipeline.results["noise_filtering"], cv2.COLOR_BGR2RGB)
    )
    axes[0, 1].set_title("Noise Filtered")
    axes[0, 1].axis("off")

    axes[0, 2].imshow(
        cv2.cvtColor(pipeline.results["contrast_enhancement"], cv2.COLOR_BGR2RGB)
    )
    axes[0, 2].set_title("Contrast Enhanced")
    axes[0, 2].axis("off")

    # Row 2: Advanced processing
    axes[1, 0].imshow(
        cv2.cvtColor(pipeline.results["image_sharpening"], cv2.COLOR_BGR2RGB)
    )
    axes[1, 0].set_title("Sharpened")
    axes[1, 0].axis("off")

    axes[1, 1].imshow(pipeline.results["edge_detection"], cmap="gray")
    axes[1, 1].set_title("Edge Detection")
    axes[1, 1].axis("off")

    # Show detected objects
    img_with_blobs = cv2.cvtColor(sample_image, cv2.COLOR_BGR2RGB).copy()
    for blob in blobs:
        y, x, r = blob
        circle = plt.Circle((x, y), r, color="red", fill=False, linewidth=2)
        axes[1, 2].add_patch(circle)
    axes[1, 2].imshow(img_with_blobs)
    axes[1, 2].set_title(f"Blob Detection ({len(blobs)} blobs)")
    axes[1, 2].axis("off")

    # Row 3: Segmentation results
    axes[2, 0].imshow(thresh_seg, cmap="gray")
    axes[2, 0].set_title("Threshold Segmentation")
    axes[2, 0].axis("off")

    axes[2, 1].imshow(cv2.cvtColor(kmeans_seg, cv2.COLOR_BGR2RGB))
    axes[2, 1].set_title("K-means Segmentation")
    axes[2, 1].axis("off")

    # Watershed with colored regions
    watershed_colored = np.zeros_like(sample_image)
    watershed_colored[watershed_seg == -1] = [0, 0, 255]  # Boundaries in red
    axes[2, 2].imshow(cv2.cvtColor(watershed_colored, cv2.COLOR_BGR2RGB))
    axes[2, 2].set_title("Watershed Segmentation")
    axes[2, 2].axis("off")

    plt.tight_layout()
    plt.savefig(
        "/Users/harshilpatel/CODE/Major/assignment_05_comprehensive_results.png",
        dpi=300,
        bbox_inches="tight",
    )
    plt.show()

    return pipeline


def main():
    """Main function to demonstrate the image processing pipeline"""
    # Run the complete demonstration
    pipeline = demonstrate_pipeline()

    # Summary
    print("\n" + "=" * 60)
    print("ASSIGNMENT 5 SUMMARY")
    print("=" * 60)

    print("\nProcessing Pipeline Steps:")
    for i, step in enumerate(pipeline.steps, 1):
        print(f"{i}. {step['name'].replace('_', ' ').title()}")

    print(f"\nKey Features Implemented:")
    print("✓ Noise Filtering (Gaussian, Median, Bilateral, Morphological)")
    print("✓ Contrast Enhancement (Histogram Equalization, CLAHE, Gamma)")
    print("✓ Image Sharpening (Unsharp Masking, Laplacian, High-pass)")
    print("✓ Object Detection (Edge, Blob, Corner, Contour)")
    print("✓ ROI Segmentation (Threshold, Watershed, K-means, Region Growing)")
    print("✓ Complete Pipeline Framework")
    print("✓ Comprehensive Visualization")

    print(f"\nTechniques Demonstrated:")
    print("• Multi-scale noise reduction")
    print("• Adaptive contrast enhancement")
    print("• Edge-preserving filtering")
    print("• Multi-method object detection")
    print("• Region-based segmentation")
    print("• End-to-end processing workflow")

    print(f"\nGenerated Files:")
    print("• assignment_05_pipeline_results.png")
    print("• assignment_05_comprehensive_results.png")

    print(f"\nApplications:")
    print("• Medical image preprocessing")
    print("• Computer vision pipelines")
    print("• Quality control systems")
    print("• Image enhancement workflows")


if __name__ == "__main__":
    main()
