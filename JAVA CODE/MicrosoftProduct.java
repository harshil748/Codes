import java.util.Scanner;
// Java Practical 2.1
public class MicrosoftProduct {
    private float productNo;
    private String productName;
    private String activationKey;
    private float priceofProduct;

    public MicrosoftProduct(float productNo, String productName, String activationKey, float priceofProduct) {
        this.productNo = productNo;
        this.productName = productName;
        this.activationKey = activationKey;
        this.priceofProduct = priceofProduct;
    }

    public String getProductName() {
        return productName;
    }

    public String getActivationKey() {
        return activationKey;
    }

    public float getProductNo() {
        return productNo;
    }

    public float getPriceofProduct() {
        return priceofProduct;
    }

    public void setActivationKey(String activationKey) {
        this.activationKey = activationKey;
    }

    public void display() {
        System.out.println("Product No: " + productNo);
        System.out.println("Product Name: " + productName);
        System.out.println("Activation Key: " + activationKey);
        System.out.println("Price of Product: " + priceofProduct);
    }

    public static void main(String[] args) {
        MicrosoftProduct[] products = new MicrosoftProduct[5];
        Scanner scanner = new Scanner(System.in);
        for (int i = 0; i < products.length; i++) {
            System.out.println("Enter details for product " + (i + 1) + ":");
            System.out.print("Product No: ");
            float productNo = scanner.nextFloat();
            scanner.nextLine();
            System.out.print("Product Name: ");
            String productName = scanner.nextLine();
            System.out.print("Activation Key: ");
            String activationKey = scanner.nextLine();
            System.out.print("Price of Product: ");
            float priceofProduct = scanner.nextFloat();
            scanner.nextLine();
            products[i] = new MicrosoftProduct(productNo, productName, activationKey, priceofProduct);
        }
        System.out.print("Enter product name to search: ");
        String searchProductName = scanner.nextLine();
        System.out.print("Enter product number to search: ");
        float searchProductNo = scanner.nextFloat();
        for (MicrosoftProduct product : products) {
            if (product.getProductName().equalsIgnoreCase(searchProductName) && product.getProductNo() == searchProductNo) {
                product.display();
                break;
            }
        }
        scanner.close();
    }
}