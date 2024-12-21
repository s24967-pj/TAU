public class InventoryService {

    public boolean checkAvailability(String product, int quantity) {
        int availableQuantity = 10;

        if (quantity <= availableQuantity) {
            System.out.println("Produkt '" + product + "' dostępny w ilości " + quantity + " sztuk.");
            return true;
        } else {
            System.out.println("Brak wystarczającej ilości produktu '" + product + "' w magazynie.");
            return false;
        }
    }
}