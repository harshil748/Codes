import requests

API_URL = "https://jsonplaceholder.typicode.com/comments"


def fetch_reviews():
    try:
        response = requests.get(API_URL, timeout=30)
        response.raise_for_status()

        data = response.json()

        if isinstance(data, list):
            return data

        if isinstance(data, dict):
            return data.get("comments", [])

        return []

    except requests.exceptions.Timeout:
        print("API error request timed out.")
        return []

    except requests.exceptions.ConnectionError:
        print("API error could not connect to the API.")
        return []

    except requests.exceptions.HTTPError as e:
        print("API error:", e)
        return []

    except requests.exceptions.RequestException as e:
        print("API error:", e)
        return []

    except ValueError:
        print("API error invalid JSON response.")
        return []


def prepare_product_reviews(data):
    product_a = []
    product_b = []

    for review in data[:50]:
        rating = (review["id"] % 5) + 1
        helpful_votes = (review["id"] * 7) % 150

        product_a.append(
            {
                "review_id": review["id"],
                "product_id": "product_a",
                "rating": rating,
                "review_text": review["body"],
                "helpful_votes": helpful_votes,
                "review_date": "2026-08-26",
            }
        )

    for review in data[50:100]:
        rating = (review["id"] % 5) + 1
        helpful_votes = (review["id"] * 7) % 150

        product_b.append(
            {
                "review_id": review["id"],
                "product_id": "product_b",
                "rating": rating,
                "review_text": review["body"],
                "helpful_votes": helpful_votes,
                "review_date": "2026-08-26",
            }
        )

    return product_a, product_b


def analyze_product(reviews):
    total_reviews = len(reviews)

    if total_reviews == 0:
        return {
            "total": 0,
            "avg_rating": 0,
            "avg_helpful": 0,
            "positive": 0,
            "negative": 0,
            "neutral": 0,
            "positive_percentage": 0,
            "negative_percentage": 0,
            "suspicious": [],
            "highly_negative": [],
        }

    avg_rating = sum(review["rating"] for review in reviews) / total_reviews

    avg_helpful = sum(review["helpful_votes"] for review in reviews) / total_reviews

    positive = sum(1 for review in reviews if review["rating"] in [4, 5])

    negative = sum(1 for review in reviews if review["rating"] in [1, 2])

    neutral = sum(1 for review in reviews if review["rating"] == 3)

    positive_percentage = (positive / total_reviews) * 100
    negative_percentage = (negative / total_reviews) * 100

    suspicious = []
    highly_negative = []

    for review in reviews:
        if review["rating"] <= 2 and review["helpful_votes"] > 50:
            suspicious.append(review)

        if review["rating"] <= 2 and len(review["review_text"]) > 100:
            highly_negative.append(review)

    return {
        "total": total_reviews,
        "avg_rating": avg_rating,
        "avg_helpful": avg_helpful,
        "positive": positive,
        "negative": negative,
        "neutral": neutral,
        "positive_percentage": positive_percentage,
        "negative_percentage": negative_percentage,
        "suspicious": suspicious,
        "highly_negative": highly_negative,
    }


def print_flagged_reviews(product_name, reviews):
    print(f"\nflagged reviews on {product_name}:")

    if not reviews:
        print("none")
        return

    for review in reviews:
        print(
            f"-> review id: {review['review_id']} "
            f"(rating: {review['rating']}, "
            f"helpful votes: {review['helpful_votes']})"
        )


def print_report(a_stats, b_stats):
    print()
    print("product review analysis report")

    print(
        f"{'product':<13}"
        f"{'total reviews':<15}"
        f"{'avg rating':<13}"
        f"{'avg helpful':<15}"
        f"{'positive':<11}"
        f"{'negative':<11}"
        f"{'suspicious'}"
    )

    print("-" * 100)

    print(
        f"{'product_a':<13}"
        f"{a_stats['total']:<15}"
        f"{a_stats['avg_rating']:<13.2f}"
        f"{a_stats['avg_helpful']:<15.2f}"
        f"{a_stats['positive']:<11}"
        f"{a_stats['negative']:<11}"
        f"{len(a_stats['suspicious'])}"
    )

    print(
        f"{'product_b':<13}"
        f"{b_stats['total']:<15}"
        f"{b_stats['avg_rating']:<13.2f}"
        f"{b_stats['avg_helpful']:<15.2f}"
        f"{b_stats['positive']:<11}"
        f"{b_stats['negative']:<11}"
        f"{len(b_stats['suspicious'])}"
    )


    print("\ndetailed comparison")

    if a_stats["avg_rating"] > b_stats["avg_rating"]:
        satisfaction = "product_a"
    elif b_stats["avg_rating"] > a_stats["avg_rating"]:
        satisfaction = "product_b"
    else:
        satisfaction = "Both products are equal"

    print(f"product with better customer satisfaction: " f"{satisfaction}")

    if a_stats["negative_percentage"] > b_stats["negative_percentage"]:
        higher_negative = "product_a"
    elif b_stats["negative_percentage"] > a_stats["negative_percentage"]:
        higher_negative = "product_b"
    else:
        higher_negative = "Both products are equal"

    print(f"product with higher negative feedback: " f"{higher_negative}")

    if len(a_stats["suspicious"]) > len(b_stats["suspicious"]):
        unusual_activity = "product_a"
    elif len(b_stats["suspicious"]) > len(a_stats["suspicious"]):
        unusual_activity = "product_b"
    else:
        unusual_activity = "Both products are equal"

    print(
        f"product with more potentially unusual review activity: " f"{unusual_activity}"
    )

    print("\naverage rating comparison:")
    print(f"product_a: {a_stats['avg_rating']:.2f}")
    print(f"product_b: {b_stats['avg_rating']:.2f}")

    print("\naverage helpful votes comparison:")
    print(f"product_a: {a_stats['avg_helpful']:.2f}")
    print(f"product_b: {b_stats['avg_helpful']:.2f}")

    print("\nPositive Review Percentage:")
    print(f"product_a: {a_stats['positive_percentage']:.2f}%")
    print(f"product_b: {b_stats['positive_percentage']:.2f}%")

    print("\nNegative Review Percentage:")
    print(f"product_a: {a_stats['negative_percentage']:.2f}%")
    print(f"product_b: {b_stats['negative_percentage']:.2f}%")

    print_flagged_reviews("product_a", a_stats["suspicious"])

    print_flagged_reviews("product_b", b_stats["suspicious"])

    all_highly_negative = a_stats["highly_negative"] + b_stats["highly_negative"]

    print("\nHighly Negative Reviews:")

    if not all_highly_negative:
        print("None")
    else:
        for review in all_highly_negative:
            print(
                f"-> review id: {review['review_id']} "
                f"(rating: {review['rating']}, "
                f"length: {len(review['review_text'])} characters)"
            )


reviews = fetch_reviews()

print(f"reviews retrieved from API: {len(reviews)}")

if len(reviews) < 100:
    print("warning fewer than 100 reviews were retrieved.")

product_a, product_b = prepare_product_reviews(reviews)

a_stats = analyze_product(product_a)
b_stats = analyze_product(product_b)

print_report(a_stats, b_stats)
