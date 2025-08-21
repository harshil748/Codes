"""
Assignment 4: Write a recursive program to compute the fractal dimensions of any shape
and plot/display the Sierpinski Triangle.
"""

import numpy as np
import matplotlib.pyplot as plt
import math
from typing import List, Tuple, Optional
import time
from matplotlib.patches import Polygon
from matplotlib.animation import FuncAnimation
import random

# ==================== FRACTAL DIMENSION COMPUTATION ====================


class FractalDimension:
    """Compute fractal dimensions using various methods"""

    @staticmethod
    def box_counting_dimension(
        points: np.ndarray,
        min_box_size: float = 0.01,
        max_box_size: float = 1.0,
        num_sizes: int = 20,
    ) -> Tuple[float, List[float], List[int]]:
        """
        Compute fractal dimension using box counting method

        Args:
            points: Array of (x, y) coordinates
            min_box_size: Minimum box size for counting
            max_box_size: Maximum box size for counting
            num_sizes: Number of different box sizes to test

        Returns:
            Fractal dimension, box sizes, and box counts
        """
        if len(points) == 0:
            return 0.0, [], []

        # Normalize points to [0, 1] range
        points_norm = points.copy()
        x_min, x_max = points[:, 0].min(), points[:, 0].max()
        y_min, y_max = points[:, 1].min(), points[:, 1].max()

        if x_max - x_min > 0:
            points_norm[:, 0] = (points[:, 0] - x_min) / (x_max - x_min)
        if y_max - y_min > 0:
            points_norm[:, 1] = (points[:, 1] - y_min) / (y_max - y_min)

        # Generate box sizes (logarithmic spacing)
        box_sizes = np.logspace(
            np.log10(min_box_size), np.log10(max_box_size), num_sizes
        )
        box_counts = []

        for box_size in box_sizes:
            # Count boxes containing points
            count = FractalDimension._count_boxes_with_points(points_norm, box_size)
            box_counts.append(count)

        # Fit line to log-log plot: log(count) = -D * log(box_size) + C
        # where D is the fractal dimension
        log_sizes = np.log(box_sizes)
        log_counts = np.log([max(1, count) for count in box_counts])  # Avoid log(0)

        # Linear regression
        if len(log_sizes) > 1:
            slope, _ = np.polyfit(log_sizes, log_counts, 1)
            fractal_dim = -slope
        else:
            fractal_dim = 0.0

        return fractal_dim, box_sizes.tolist(), box_counts

    @staticmethod
    def _count_boxes_with_points(points: np.ndarray, box_size: float) -> int:
        """Count number of boxes of given size that contain at least one point"""
        if box_size <= 0:
            return 0

        # Create grid of boxes
        num_boxes = int(1.0 / box_size) + 1
        occupied_boxes = set()

        for point in points:
            # Find which box this point belongs to
            box_x = int(point[0] / box_size)
            box_y = int(point[1] / box_size)
            occupied_boxes.add((box_x, box_y))

        return len(occupied_boxes)

    @staticmethod
    def hausdorff_dimension_estimate(
        points: np.ndarray, num_radii: int = 20, max_points: int = 2000
    ) -> Tuple[float, List[float], List[float]]:
        """
        Estimate Hausdorff dimension using correlation sum method

        Args:
            points: Array of (x, y) coordinates
            num_radii: Number of different radii to test
            max_points: Maximum number of points to use (for performance)

        Returns:
            Estimated Hausdorff dimension, radii, and correlation sums
        """
        if len(points) < 2:
            return 0.0, [], []

        # Subsample points if too many (for performance)
        if len(points) > max_points:
            indices = np.random.choice(len(points), max_points, replace=False)
            points = points[indices]

        # Calculate distance matrix
        distances = []
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                dist = np.linalg.norm(points[i] - points[j])
                distances.append(dist)

        distances = np.array(distances)
        max_dist = distances.max()
        min_dist = (
            distances[distances > 0].min()
            if len(distances[distances > 0]) > 0
            else max_dist / 1000
        )

        # Generate radii (logarithmic spacing)
        radii = np.logspace(np.log10(min_dist), np.log10(max_dist / 2), num_radii)
        correlation_sums = []

        for radius in radii:
            # Count pairs within radius
            count = np.sum(distances <= radius)
            # Normalize by total number of pairs
            correlation_sum = count / len(distances)
            correlation_sums.append(correlation_sum)

        # Fit line to log-log plot
        log_radii = np.log(radii)
        log_sums = np.log([max(1e-10, cs) for cs in correlation_sums])

        # Linear regression on the linear part (middle section)
        if len(log_radii) > 4:
            start_idx = len(log_radii) // 4
            end_idx = 3 * len(log_radii) // 4
            slope, _ = np.polyfit(
                log_radii[start_idx:end_idx], log_sums[start_idx:end_idx], 1
            )
            hausdorff_dim = slope
        else:
            hausdorff_dim = 0.0

        return hausdorff_dim, radii.tolist(), correlation_sums


# ==================== SIERPINSKI TRIANGLE IMPLEMENTATION ====================


class SierpinskiTriangle:
    """Recursive implementation of Sierpinski Triangle"""

    def __init__(self):
        self.points = []
        self.triangles = []

    def generate_recursive(self, vertices: List[Tuple[float, float]], depth: int):
        """
        Generate Sierpinski triangle recursively

        Args:
            vertices: Three vertices of the initial triangle [(x1,y1), (x2,y2), (x3,y3)]
            depth: Recursion depth (number of iterations)
        """
        self.points = []
        self.triangles = []
        self._recursive_subdivide(vertices, depth)
        return np.array(self.points)

    def _recursive_subdivide(self, vertices: List[Tuple[float, float]], depth: int):
        """Recursively subdivide triangle"""
        if depth == 0:
            # Base case: add triangle vertices to points
            for vertex in vertices:
                self.points.append(vertex)
            self.triangles.append(vertices.copy())
            return

        # Calculate midpoints of each edge
        v1, v2, v3 = vertices
        mid12 = ((v1[0] + v2[0]) / 2, (v1[1] + v2[1]) / 2)
        mid23 = ((v2[0] + v3[0]) / 2, (v2[1] + v3[1]) / 2)
        mid13 = ((v1[0] + v3[0]) / 2, (v1[1] + v3[1]) / 2)

        # Recursively create three smaller triangles
        self._recursive_subdivide([v1, mid12, mid13], depth - 1)
        self._recursive_subdivide([mid12, v2, mid23], depth - 1)
        self._recursive_subdivide([mid13, mid23, v3], depth - 1)

    def generate_chaos_game(
        self,
        num_points: int = 10000,
        vertices: Optional[List[Tuple[float, float]]] = None,
    ) -> np.ndarray:
        """
        Generate Sierpinski triangle using chaos game method

        Args:
            num_points: Number of points to generate
            vertices: Triangle vertices (defaults to equilateral triangle)

        Returns:
            Array of generated points
        """
        if vertices is None:
            # Default equilateral triangle
            vertices = [(0, 0), (1, 0), (0.5, np.sqrt(3) / 2)]

        # Convert to numpy array for easier computation
        vertices_array = np.array(vertices)

        # Start with random point inside triangle
        current_point = np.mean(vertices_array, axis=0)
        points = [current_point.copy()]

        for _ in range(num_points - 1):
            # Randomly choose one of the three vertices
            chosen_vertex = vertices_array[random.randint(0, 2)]

            # Move halfway toward chosen vertex
            current_point = (current_point + chosen_vertex) / 2
            points.append(current_point.copy())

        self.points = points
        return np.array(points)

    def generate_ifs(self, num_points: int = 10000) -> np.ndarray:
        """
        Generate Sierpinski triangle using Iterated Function System (IFS)

        Args:
            num_points: Number of points to generate

        Returns:
            Array of generated points
        """
        # IFS transformations for Sierpinski triangle
        transformations = [
            # T1: scale by 0.5, no translation
            lambda x, y: (0.5 * x, 0.5 * y),
            # T2: scale by 0.5, translate by (0.5, 0)
            lambda x, y: (0.5 * x + 0.5, 0.5 * y),
            # T3: scale by 0.5, translate by (0.25, sqrt(3)/4)
            lambda x, y: (0.5 * x + 0.25, 0.5 * y + np.sqrt(3) / 4),
        ]

        # Start with random point
        x, y = random.random(), random.random()
        points = [(x, y)]

        for _ in range(num_points - 1):
            # Randomly choose transformation
            transform = random.choice(transformations)
            x, y = transform(x, y)
            points.append((x, y))

        self.points = points
        return np.array(points)


# ==================== FRACTAL SHAPES FOR TESTING ====================


class FractalShapes:
    """Generate various fractal shapes for dimension testing"""

    @staticmethod
    def koch_snowflake(iterations: int = 4) -> np.ndarray:
        """Generate Koch snowflake fractal"""
        # Start with equilateral triangle
        vertices = np.array(
            [[0, 0], [1, 0], [0.5, np.sqrt(3) / 2], [0, 0]]  # Close the triangle
        )

        for _ in range(iterations):
            new_vertices = [vertices[0]]

            for i in range(len(vertices) - 1):
                p1, p2 = vertices[i], vertices[i + 1]

                # Divide edge into three parts
                one_third = p1 + (p2 - p1) / 3
                two_third = p1 + 2 * (p2 - p1) / 3

                # Create equilateral triangle on middle third
                direction = p2 - p1
                perpendicular = np.array([-direction[1], direction[0]])
                perpendicular = perpendicular / np.linalg.norm(perpendicular)
                height = np.linalg.norm(p2 - p1) / (2 * np.sqrt(3))
                peak = (one_third + two_third) / 2 + height * perpendicular

                new_vertices.extend([one_third, peak, two_third, p2])

            vertices = np.array(new_vertices)

        return vertices

    @staticmethod
    def dragon_curve(iterations: int = 10) -> np.ndarray:
        """Generate Dragon curve fractal"""
        directions = [0]  # 0 = right, 1 = up, 2 = left, 3 = down

        for _ in range(iterations):
            # Add turn in middle, then reverse and add opposite turns
            new_directions = (
                directions + [1] + [(d + 2) % 4 for d in reversed(directions)]
            )
            directions = new_directions

        # Convert directions to points
        x, y = 0, 0
        points = [(x, y)]

        for direction in directions:
            if direction == 0:  # right
                x += 1
            elif direction == 1:  # up
                y += 1
            elif direction == 2:  # left
                x -= 1
            elif direction == 3:  # down
                y -= 1
            points.append((x, y))

        return np.array(points)

    @staticmethod
    def cantor_dust(iterations: int = 6) -> np.ndarray:
        """Generate 2D Cantor dust (Cantor set × Cantor set)"""
        # Start with unit square
        squares = [[(0, 0), (1, 1)]]

        for _ in range(iterations):
            new_squares = []
            for (x1, y1), (x2, y2) in squares:
                width = x2 - x1
                height = y2 - y1

                # Divide into 9 squares, keep corners and middle edges (remove center and cross)
                positions = [
                    (0, 0),
                    (1 / 3, 0),
                    (2 / 3, 0),
                    (0, 1 / 3),
                    (2 / 3, 1 / 3),
                    (0, 2 / 3),
                    (1 / 3, 2 / 3),
                    (2 / 3, 2 / 3),
                ]

                for px, py in positions:
                    nx1 = x1 + px * width
                    ny1 = y1 + py * height
                    nx2 = nx1 + width / 3
                    ny2 = ny1 + height / 3
                    new_squares.append([(nx1, ny1), (nx2, ny2)])

            squares = new_squares

        # Convert squares to points
        points = []
        for (x1, y1), (x2, y2) in squares:
            # Sample points from each square
            for i in range(5):
                for j in range(5):
                    x = x1 + (x2 - x1) * i / 4
                    y = y1 + (y2 - y1) * j / 4
                    points.append((x, y))

        return np.array(points)


# ==================== VISUALIZATION ====================


class FractalVisualizer:
    """Visualize fractals and their dimensional analysis"""

    @staticmethod
    def plot_sierpinski_comparison(sierpinski: SierpinskiTriangle):
        """Compare different methods of generating Sierpinski triangle"""
        fig, axes = plt.subplots(2, 2, figsize=(12, 12))

        # Method 1: Recursive subdivision
        vertices = [(0, 0), (1, 0), (0.5, np.sqrt(3) / 2)]
        points_recursive = sierpinski.generate_recursive(vertices, 6)
        axes[0, 0].scatter(
            points_recursive[:, 0], points_recursive[:, 1], s=0.1, c="blue", alpha=0.7
        )
        axes[0, 0].set_title("Recursive Subdivision (Depth 6)")
        axes[0, 0].set_aspect("equal")

        # Method 2: Chaos game
        points_chaos = sierpinski.generate_chaos_game(20000)
        axes[0, 1].scatter(
            points_chaos[:, 0], points_chaos[:, 1], s=0.1, c="red", alpha=0.7
        )
        axes[0, 1].set_title("Chaos Game (20k points)")
        axes[0, 1].set_aspect("equal")

        # Method 3: IFS
        points_ifs = sierpinski.generate_ifs(20000)
        axes[1, 0].scatter(
            points_ifs[:, 0], points_ifs[:, 1], s=0.1, c="green", alpha=0.7
        )
        axes[1, 0].set_title("Iterated Function System (20k points)")
        axes[1, 0].set_aspect("equal")

        # Method 4: All overlaid
        axes[1, 1].scatter(
            points_recursive[:, 0],
            points_recursive[:, 1],
            s=0.5,
            c="blue",
            alpha=0.5,
            label="Recursive",
        )
        axes[1, 1].scatter(
            points_chaos[::10, 0],
            points_chaos[::10, 1],
            s=0.1,
            c="red",
            alpha=0.5,
            label="Chaos Game",
        )
        axes[1, 1].scatter(
            points_ifs[::10, 0],
            points_ifs[::10, 1],
            s=0.1,
            c="green",
            alpha=0.5,
            label="IFS",
        )
        axes[1, 1].set_title("All Methods Overlaid")
        axes[1, 1].set_aspect("equal")
        axes[1, 1].legend()

        plt.tight_layout()
        return fig

    @staticmethod
    def plot_fractal_dimension_analysis(points: np.ndarray, shape_name: str):
        """Plot fractal dimension analysis"""
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))

        # Original shape
        axes[0, 0].scatter(points[:, 0], points[:, 1], s=0.5, alpha=0.7)
        axes[0, 0].set_title(f"{shape_name} - Original Shape")
        axes[0, 0].set_aspect("equal")

        # Box counting analysis
        box_dim, box_sizes, box_counts = FractalDimension.box_counting_dimension(points)
        axes[0, 1].loglog(box_sizes, box_counts, "bo-", markersize=4)
        axes[0, 1].set_xlabel("Box Size")
        axes[0, 1].set_ylabel("Number of Boxes")
        axes[0, 1].set_title(f"Box Counting Method\nDimension: {box_dim:.3f}")
        axes[0, 1].grid(True, alpha=0.3)

        # Hausdorff dimension estimate
        hausdorff_dim, radii, corr_sums = FractalDimension.hausdorff_dimension_estimate(
            points
        )
        axes[1, 0].loglog(radii, corr_sums, "ro-", markersize=4)
        axes[1, 0].set_xlabel("Radius")
        axes[1, 0].set_ylabel("Correlation Sum")
        axes[1, 0].set_title(
            f"Hausdorff Dimension Estimate\nDimension: {hausdorff_dim:.3f}"
        )
        axes[1, 0].grid(True, alpha=0.3)

        # Box counting visualization
        FractalVisualizer._visualize_box_counting(axes[1, 1], points, box_size=0.1)
        axes[1, 1].set_title("Box Counting Visualization (box size = 0.1)")

        plt.tight_layout()
        return fig, box_dim, hausdorff_dim

    @staticmethod
    def _visualize_box_counting(ax, points: np.ndarray, box_size: float = 0.1):
        """Visualize the box counting process"""
        # Normalize points
        points_norm = points.copy()
        x_min, x_max = points[:, 0].min(), points[:, 0].max()
        y_min, y_max = points[:, 1].min(), points[:, 1].max()

        if x_max - x_min > 0:
            points_norm[:, 0] = (points[:, 0] - x_min) / (x_max - x_min)
        if y_max - y_min > 0:
            points_norm[:, 1] = (points[:, 1] - y_min) / (y_max - y_min)

        # Plot points
        ax.scatter(points_norm[:, 0], points_norm[:, 1], s=1, alpha=0.7, c="blue")

        # Draw grid and highlight occupied boxes
        num_boxes = int(1.0 / box_size) + 1
        occupied_boxes = set()

        for point in points_norm:
            box_x = int(point[0] / box_size)
            box_y = int(point[1] / box_size)
            occupied_boxes.add((box_x, box_y))

        # Draw grid lines
        for i in range(num_boxes + 1):
            ax.axvline(i * box_size, color="gray", alpha=0.3, linewidth=0.5)
            ax.axhline(i * box_size, color="gray", alpha=0.3, linewidth=0.5)

        # Highlight occupied boxes
        for box_x, box_y in occupied_boxes:
            rect = plt.Rectangle(
                (box_x * box_size, box_y * box_size),
                box_size,
                box_size,
                fill=False,
                edgecolor="red",
                linewidth=1.5,
            )
            ax.add_patch(rect)

        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_aspect("equal")


# ==================== MAIN DEMONSTRATION ====================


def demonstrate_sierpinski_triangle():
    """Demonstrate Sierpinski triangle generation and analysis"""
    print("=== Sierpinski Triangle Demonstration ===")

    sierpinski = SierpinskiTriangle()

    # Generate using different methods
    print("Generating Sierpinski triangle using different methods...")

    # Recursive method
    vertices = [(0, 0), (1, 0), (0.5, np.sqrt(3) / 2)]
    points_recursive = sierpinski.generate_recursive(vertices, 7)
    print(f"Recursive method (depth 7): {len(points_recursive)} points")

    # Chaos game method
    points_chaos = sierpinski.generate_chaos_game(10000)
    print(f"Chaos game method: {len(points_chaos)} points")

    # IFS method
    points_ifs = sierpinski.generate_ifs(10000)
    print(f"IFS method: {len(points_ifs)} points")

    # Visualize comparison
    fig1 = FractalVisualizer.plot_sierpinski_comparison(sierpinski)
    plt.savefig(
        "/Users/harshilpatel/CODE/Major/assignment_04_sierpinski_comparison.png",
        dpi=300,
        bbox_inches="tight",
    )
    plt.show()

    # Analyze fractal dimension
    print("\nAnalyzing fractal dimensions...")
    fig2, box_dim, hausdorff_dim = FractalVisualizer.plot_fractal_dimension_analysis(
        points_chaos, "Sierpinski Triangle"
    )
    plt.savefig(
        "/Users/harshilpatel/CODE/Major/assignment_04_sierpinski_analysis.png",
        dpi=300,
        bbox_inches="tight",
    )
    plt.show()

    print(f"Sierpinski Triangle - Box counting dimension: {box_dim:.3f}")
    print(f"Sierpinski Triangle - Hausdorff dimension estimate: {hausdorff_dim:.3f}")
    print(f"Theoretical dimension: {math.log(3)/math.log(2):.3f}")

    return points_chaos, box_dim, hausdorff_dim


def demonstrate_fractal_shapes():
    """Demonstrate various fractal shapes and their dimensions"""
    print("\n=== Various Fractal Shapes Analysis ===")

    shapes = FractalShapes()
    results = {}

    # Koch snowflake
    print("Analyzing Koch snowflake...")
    koch_points = shapes.koch_snowflake(5)
    fig3, koch_box_dim, koch_hausdorff_dim = (
        FractalVisualizer.plot_fractal_dimension_analysis(koch_points, "Koch Snowflake")
    )
    plt.savefig(
        "/Users/harshilpatel/CODE/Major/assignment_04_koch_analysis.png",
        dpi=300,
        bbox_inches="tight",
    )
    plt.show()

    theoretical_koch = math.log(4) / math.log(3)
    results["Koch Snowflake"] = {
        "box_counting": koch_box_dim,
        "hausdorff": koch_hausdorff_dim,
        "theoretical": theoretical_koch,
    }

    # Dragon curve
    print("Analyzing Dragon curve...")
    dragon_points = shapes.dragon_curve(12)
    fig4, dragon_box_dim, dragon_hausdorff_dim = (
        FractalVisualizer.plot_fractal_dimension_analysis(dragon_points, "Dragon Curve")
    )
    plt.savefig(
        "/Users/harshilpatel/CODE/Major/assignment_04_dragon_analysis.png",
        dpi=300,
        bbox_inches="tight",
    )
    plt.show()

    results["Dragon Curve"] = {
        "box_counting": dragon_box_dim,
        "hausdorff": dragon_hausdorff_dim,
        "theoretical": 2.0,  # Dragon curve fills plane
    }

    # Cantor dust
    print("Analyzing Cantor dust...")
    cantor_points = shapes.cantor_dust(5)
    fig5, cantor_box_dim, cantor_hausdorff_dim = (
        FractalVisualizer.plot_fractal_dimension_analysis(cantor_points, "Cantor Dust")
    )
    plt.savefig(
        "/Users/harshilpatel/CODE/Major/assignment_04_cantor_analysis.png",
        dpi=300,
        bbox_inches="tight",
    )
    plt.show()

    theoretical_cantor = 2 * math.log(2) / math.log(3)  # log_3(4)
    results["Cantor Dust"] = {
        "box_counting": cantor_box_dim,
        "hausdorff": cantor_hausdorff_dim,
        "theoretical": theoretical_cantor,
    }

    return results


def create_animated_sierpinski():
    """Create an animation showing Sierpinski triangle formation"""
    print("\nCreating animated Sierpinski triangle formation...")

    sierpinski = SierpinskiTriangle()

    # Generate points progressively
    max_depth = 7
    frames_data = []

    vertices = [(0, 0), (1, 0), (0.5, np.sqrt(3) / 2)]

    for depth in range(max_depth + 1):
        points = sierpinski.generate_recursive(vertices, depth)
        frames_data.append(points)

    # Create animation
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(-0.1, 1.0)
    ax.set_aspect("equal")
    ax.set_title("Sierpinski Triangle Formation (Recursive Method)")

    def animate(frame):
        ax.clear()
        ax.set_xlim(-0.1, 1.1)
        ax.set_ylim(-0.1, 1.0)
        ax.set_aspect("equal")
        ax.set_title(f"Sierpinski Triangle - Depth {frame}")

        if frame < len(frames_data):
            points = frames_data[frame]
            if len(points) > 0:
                ax.scatter(points[:, 0], points[:, 1], s=2, c="blue", alpha=0.7)

        return ax.collections

    try:
        anim = FuncAnimation(
            fig, animate, frames=max_depth + 1, interval=1000, blit=False
        )
        anim.save(
            "/Users/harshilpatel/CODE/Major/assignment_04_sierpinski_animation.gif",
            writer="pillow",
            fps=1,
        )
        print("Animation saved as assignment_04_sierpinski_animation.gif")
    except Exception as e:
        print(f"Animation creation failed: {e}")

    plt.close()


def main():
    """Main function to demonstrate fractal dimensions and Sierpinski triangle"""
    print("Assignment 4: Fractal Dimensions and Sierpinski Triangle")
    print("=" * 70)

    # Simple demonstration without heavy computation
    sierpinski = SierpinskiTriangle()

    print("\n=== Sierpinski Triangle Generation ===")

    # Generate using different methods (smaller sizes)
    vertices = [(0, 0), (1, 0), (0.5, np.sqrt(3) / 2)]
    points_recursive = sierpinski.generate_recursive(vertices, 5)
    print(f"Recursive method (depth 5): {len(points_recursive)} points")

    points_chaos = sierpinski.generate_chaos_game(5000)
    print(f"Chaos game method: {len(points_chaos)} points")

    points_ifs = sierpinski.generate_ifs(5000)
    print(f"IFS method: {len(points_ifs)} points")

    # Quick visualization
    fig1 = FractalVisualizer.plot_sierpinski_comparison(sierpinski)
    plt.savefig(
        "/Users/harshilpatel/CODE/Major/assignment_04_sierpinski_comparison.png",
        dpi=300,
        bbox_inches="tight",
    )
    plt.show()

    # Quick fractal dimension analysis (smaller dataset)
    print("\n=== Fractal Dimension Analysis ===")
    box_dim, box_sizes, box_counts = FractalDimension.box_counting_dimension(
        points_chaos[:1000]
    )
    print(f"Box counting dimension: {box_dim:.3f}")

    theoretical_sierpinski = math.log(3) / math.log(2)
    print(f"Theoretical Sierpinski dimension: {theoretical_sierpinski:.3f}")

    # Generate other fractals (smaller sizes)
    print("\n=== Other Fractal Shapes ===")
    shapes = FractalShapes()

    koch_points = shapes.koch_snowflake(4)
    theoretical_koch = math.log(4) / math.log(3)
    print(f"Koch snowflake generated: {len(koch_points)} points")
    print(f"Theoretical Koch dimension: {theoretical_koch:.3f}")

    dragon_points = shapes.dragon_curve(10)
    print(f"Dragon curve generated: {len(dragon_points)} points")

    cantor_points = shapes.cantor_dust(4)
    theoretical_cantor = 2 * math.log(2) / math.log(3)
    print(f"Cantor dust generated: {len(cantor_points)} points")
    print(f"Theoretical Cantor dimension: {theoretical_cantor:.3f}")

    # Create simple visualizations
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    axes[0, 0].scatter(
        points_chaos[:, 0], points_chaos[:, 1], s=0.5, alpha=0.7, c="blue"
    )
    axes[0, 0].set_title("Sierpinski Triangle (Chaos Game)")
    axes[0, 0].set_aspect("equal")

    axes[0, 1].plot(koch_points[:, 0], koch_points[:, 1], "r-", linewidth=0.8)
    axes[0, 1].set_title("Koch Snowflake")
    axes[0, 1].set_aspect("equal")

    axes[1, 0].plot(dragon_points[:, 0], dragon_points[:, 1], "g-", linewidth=0.8)
    axes[1, 0].set_title("Dragon Curve")
    axes[1, 0].set_aspect("equal")

    axes[1, 1].scatter(
        cantor_points[:, 0], cantor_points[:, 1], s=1, alpha=0.7, c="purple"
    )
    axes[1, 1].set_title("Cantor Dust")
    axes[1, 1].set_aspect("equal")

    plt.tight_layout()
    plt.savefig(
        "/Users/harshilpatel/CODE/Major/assignment_04_fractal_shapes.png",
        dpi=300,
        bbox_inches="tight",
    )
    plt.show()

    # Summary
    print("\n" + "=" * 70)
    print("ASSIGNMENT 4 SUMMARY")
    print("=" * 70)
    print("\nFeatures Implemented:")
    print("✓ Recursive Sierpinski triangle generation")
    print("✓ Chaos game method for fractal generation")
    print("✓ Iterated Function System (IFS) method")
    print("✓ Box counting fractal dimension calculation")
    print("✓ Multiple fractal shapes (Koch, Dragon, Cantor)")
    print("✓ Fractal visualization and comparison")
    print("✓ Theoretical vs computed dimension analysis")

    print(f"\nFractal Dimensions (Theoretical):")
    print(f"• Sierpinski Triangle: {theoretical_sierpinski:.3f}")
    print(f"• Koch Snowflake: {theoretical_koch:.3f}")
    print(f"• Cantor Dust: {theoretical_cantor:.3f}")

    print(f"\nGenerated Files:")
    print("• assignment_04_sierpinski_comparison.png")
    print("• assignment_04_fractal_shapes.png")

    print(f"\nKey Mathematical Concepts:")
    print("• Self-similarity in fractal structures")
    print("• Fractal dimension as measure of complexity")
    print("• Box counting method for dimension calculation")
    print("• Recursive algorithms for fractal generation")


if __name__ == "__main__":
    main()
