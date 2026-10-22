import java.util.*;
record Event(String id,String title,int capacity){}
class TicketService{
 private final Map<String,Event> events=new HashMap<>(); private final Map<String,Set<String>> bookings=new HashMap<>();
 synchronized void add(Event e){ if(e.capacity()<=0) throw new IllegalArgumentException("capacity"); if(events.putIfAbsent(e.id(),e)!=null) throw new IllegalArgumentException("duplicate"); bookings.put(e.id(),new HashSet<>()); }
 synchronized void book(String eventId,String userId){ Event e=events.get(eventId); if(e==null) throw new IllegalArgumentException("event"); Set<String>b=bookings.get(eventId); if(b.contains(userId)) throw new IllegalStateException("duplicate booking"); if(b.size()>=e.capacity()) throw new IllegalStateException("sold out"); b.add(userId); }
 synchronized void cancel(String eventId,String userId){ if(!bookings.containsKey(eventId)) throw new IllegalArgumentException("event"); if(!bookings.get(eventId).remove(userId)) throw new IllegalStateException("missing"); }
 synchronized int booked(String eventId){ if(!bookings.containsKey(eventId)) throw new IllegalArgumentException("event"); return bookings.get(eventId).size(); }
}
public class Ticketing{public static void main(String[]a){TicketService s=new TicketService();s.add(new Event("E1","Demo",2));s.book("E1","U1");System.out.println(s.booked("E1"));}}
