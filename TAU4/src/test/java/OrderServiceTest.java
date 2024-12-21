import static org.mockito.Mockito.*;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class OrderServiceTest {

    private PaymentService paymentService;
    private InventoryService inventoryService;
    private NotificationService notificationService;
    private OrderService orderService;

    @BeforeEach
    public void setUp() {
        paymentService = mock(PaymentService.class);
        inventoryService = mock(InventoryService.class);
        notificationService = mock(NotificationService.class);

        orderService = new OrderService(paymentService, inventoryService, notificationService);
    }

    @Test
    public void testOrderSuccess() {
        when(inventoryService.checkAvailability("Produkt1", 5)).thenReturn(true);
        when(paymentService.processPayment(100.0)).thenReturn(true);

        String result = orderService.placeOrder("Produkt1", 5, 100.0);

        assertEquals("Zamówienie przyjęte", result);

        verify(notificationService).sendNotification("Zamówienie na Produkt1 zrealizowane pomyślnie. Dziękujemy!");
    }

    @Test
    public void testPaymentFailure() {
        when(inventoryService.checkAvailability("Produkt1", 5)).thenReturn(true);
        when(paymentService.processPayment(100.0)).thenReturn(false);

        String result = orderService.placeOrder("Produkt1", 5, 100.0);

        assertEquals("Zamówienie odrzucone - problem z płatnością", result);

        verify(notificationService).sendNotification("Zamówienie na Produkt1 nie powiodło się - problem z płatnością.");
    }

    @Test
    public void testNotAvailable() {
        when(inventoryService.checkAvailability("Produkt1", 5)).thenReturn(false);

        String result = orderService.placeOrder("Produkt1", 5, 100.0);

        assertEquals("Zamówienie odrzucone - brak zapasów", result);

        verify(notificationService).sendNotification("Zamówienie na Produkt1 odrzucone - brak wystarczających zapasów.");
    }

    @Test
    public void testException() {
        when(inventoryService.checkAvailability("Produkt1", 5)).thenReturn(true);
        when(paymentService.processPayment(100.0)).thenThrow(new RuntimeException("Błąd płatności"));

        String result = orderService.placeOrder("Produkt1", 5, 100.0);

        assertEquals("Zamówienie odrzucone - problem z płatnością", result);

        verify(notificationService).sendNotification("Zamówienie na Produkt1 nie powiodło się - problem z płatnością.");
    }
}