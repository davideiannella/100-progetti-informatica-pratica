import java.util.*;
interface Channel{String send(String target,String message);}
class EmailChannel implements Channel{public String send(String t,String m){return "EMAIL:"+t+":"+m;}}
class SmsChannel implements Channel{public String send(String t,String m){return "SMS:"+t+":"+m;}}
class NotificationService{private final Map<String,Channel> channels=new HashMap<>();void register(String name,Channel c){channels.put(name,c);}String notify(String ch,String target,String msg){Channel c=channels.get(ch);if(c==null)throw new IllegalArgumentException("channel");return c.send(target,msg);}}
public class Notifications{public static void main(String[]a){NotificationService s=new NotificationService();s.register("email",new EmailChannel());System.out.println(s.notify("email","a@b.it","ciao"));}}
