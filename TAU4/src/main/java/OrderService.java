public class OrderService {

    private PaymentService paymentService;
    private InventoryService inventoryService;
    private NotificationService notificationService;

    public OrderService(PaymentService paymentService, InventoryService inventoryService, NotificationService notificationService) {
        this.paymentService = paymentService;
        this.inventoryService = inventoryService;
        this.notificationService = notificationService;
    }

    public String placeOrder(String product, int quantity, double amount) {
        System.out.println("Przyjmowanie zamówienia na produkt: " + product + ", ilość: " + quantity + ", cena: " + amount + " PLN");

        if (!inventoryService.checkAvailability(product, quantity)) {
            notificationService.sendNotification("Zamówienie na " + product + " odrzucone - brak wystarczających zapasów.");
            return "Zamówienie odrzucone - brak zapasów";
        }
        if (!paymentService.processPayment(amount)) {
            notificationService.sendNotification("Zamówienie na " + product + " nie powiodło się - problem z płatnością.");
            return "Zamówienie odrzucone - problem z płatnością";
        }

        notificationService.sendNotification("Zamówienie na " + product + " zrealizowane pomyślnie. Dziękujemy!");
        return "Zamówienie przyjęte";
    }

    public static void main(String[] args) {
        PaymentService paymentService = new PaymentService();
        InventoryService inventoryService = new InventoryService();
        NotificationService notificationService = new NotificationService();

        OrderService orderService = new OrderService(paymentService, inventoryService, notificationService);

        String result = orderService.placeOrder("Produkt1", 5, 100.0);
        System.out.println(result);

        result = orderService.placeOrder("Produkt1", 15, 150.0);
        System.out.println(result);
    }
}
