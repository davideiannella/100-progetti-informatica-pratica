import java.util.*;
enum OrderStatus{CREATED,ACCEPTED,PREPARING,READY,DELIVERED}
record Order(String id,String restaurantId,int totalCents,OrderStatus status){}
class OrderService{private final Map<String,Order> m=new HashMap<>();void create(String id,String r,int total){if(total<=0)throw new IllegalArgumentException();if(m.putIfAbsent(id,new Order(id,r,total,OrderStatus.CREATED))!=null) throw new IllegalArgumentException("duplicate");}void transition(String id,OrderStatus s){Order o=m.get(id);if(o==null || s==null)throw new IllegalArgumentException();m.put(id,new Order(o.id(),o.restaurantId(),o.totalCents(),s));}Order get(String id){return m.get(id);}}
class DeliveryService{int etaMinutes(int distanceKm){if(distanceKm<0)throw new IllegalArgumentException();return Math.addExact(10,Math.multiplyExact(distanceKm,3));}}
public class FoodDelivery{public static void main(String[]a){OrderService s=new OrderService();s.create("O1","R1",2200);System.out.println(s.get("O1"));}}
