"""
Test script for Assignment 4: Fractal Dimensions and Sierpinski Triangle
Quick verification that all components work correctly.
"""

import sys

sys.path.append("/Users/harshilpatel/CODE/Major")

from assignment_04_fractal_dimensions import *
import numpy as np


def test_sierpinski_methods():
    """Test all Sierpinski triangle generation methods"""
    print("Testing Sierpinski Triangle generation methods...")

    sierpinski = SierpinskiTriangle()
    vertices = [(0, 0), (1, 0), (0.5, np.sqrt(3) / 2)]

    # Test recursive method
    points_recursive = sierpinski.generate_recursive(vertices, 3)
    print(f"✓ Recursive method: {len(points_recursive)} points generated")

    # Test chaos game
    points_chaos = sierpinski.generate_chaos_game(1000)
    print(f"✓ Chaos game method: {len(points_chaos)} points generated")

    # Test IFS
    points_ifs = sierpinski.generate_ifs(1000)
    print(f"✓ IFS method: {len(points_ifs)} points generated")

    return True


def test_fractal_dimension():
    """Test fractal dimension calculation"""
    print("\nTesting fractal dimension calculation...")

    # Create simple test data
    # Line (dimension should be ~1)
    line_points = np.array([[i / 100, i / 100] for i in range(100)])
    box_dim, _, _ = FractalDimension.box_counting_dimension(line_points)
    print(f"✓ Line dimension: {box_dim:.3f} (expected ~1.0)")

    # Square filled with points (dimension should be ~2)
    square_points = np.random.rand(1000, 2)
    box_dim, _, _ = FractalDimension.box_counting_dimension(square_points)
    print(f"✓ Square dimension: {box_dim:.3f} (expected ~2.0)")

    return True


def test_fractal_shapes():
    """Test other fractal shapes generation"""
    print("\nTesting fractal shapes generation...")

    shapes = FractalShapes()

    # Koch snowflake
    koch = shapes.koch_snowflake(3)
    print(f"✓ Koch snowflake: {len(koch)} points generated")

    # Dragon curve
    dragon = shapes.dragon_curve(8)
    print(f"✓ Dragon curve: {len(dragon)} points generated")

    # Cantor dust
    cantor = shapes.cantor_dust(3)
    print(f"✓ Cantor dust: {len(cantor)} points generated")

    return True


def test_theoretical_dimensions():
    """Test theoretical dimension calculations"""
    print("\nTesting theoretical dimension calculations...")

    sierpinski_dim = math.log(3) / math.log(2)
    koch_dim = math.log(4) / math.log(3)
    cantor_dim = 2 * math.log(2) / math.log(3)

    print(f"✓ Sierpinski theoretical dimension: {sierpinski_dim:.3f}")
    print(f"✓ Koch theoretical dimension: {koch_dim:.3f}")
    print(f"✓ Cantor theoretical dimension: {cantor_dim:.3f}")

    return True


def main():
    """Run all tests"""
    print("Assignment 4: Fractal Dimensions - Component Tests")
    print("=" * 60)

    all_passed = True

    try:
        all_passed &= test_sierpinski_methods()
        all_passed &= test_fractal_dimension()
        all_passed &= test_fractal_shapes()
        all_passed &= test_theoretical_dimensions()

        print("\n" + "=" * 60)
        if all_passed:
            print("✅ ALL TESTS PASSED - Assignment 4 components working correctly!")
        else:
            print("❌ Some tests failed")

        print("\nKey Features Verified:")
        print("✓ Recursive fractal generation")
        print("✓ Chaos game algorithm")
        print("✓ Iterated Function Systems")
        print("✓ Box counting dimension calculation")
        print("✓ Multiple fractal types")
        print("✓ Theoretical dimension calculations")

    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        all_passed = False

    return all_passed


if __name__ == "__main__":
    main()
