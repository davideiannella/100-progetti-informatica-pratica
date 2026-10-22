public class FoodDeliveryLimitsTest {
    public static void main(String[] args) {
        DeliveryService delivery = new DeliveryService();
        boolean overflow = false;
        try { delivery.etaMinutes(Integer.MAX_VALUE); }
        catch (ArithmeticException e) { overflow = true; }
        assert overflow : "Una distanza positiva non deve produrre minuti negativi";
        OrderService orders = new OrderService();
        orders.create("O", "R", 10);
        boolean invalid = false;
        try { orders.transition("O", null); }
        catch (IllegalArgumentException e) { invalid = true; }
        assert invalid : "Lo stato non può essere null";
        assert orders.get("O").status() == OrderStatus.CREATED;
        System.out.println("P039: overflow ETA e stato nullo PASS");
    }
}
