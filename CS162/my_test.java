public class my_test
{

    public static void main(String args[]) 
    { 
        DLinkedList<Person> people = new DLinkedList<>();
        
        people.addLast(new Person("Bill Gates", 55));
        people.addLast(new Person("Steve Jobs", 35));
        people.addLast(new Person("Elon Musk", 42));
        people.addLast(new Person("Charlie Day", 25));
        people.addLast(new Person("Cpt. Crunch", 15));
        System.out.println(people.toString());
        for (Person p : people) { System.out.println(p.toString()); }
        
        System.out.println("");
        System.out.println("Removing Steve (RIP)");
        people.delete(1);
        for (Person p : people) { System.out.println(p.toString()); }
        
        System.out.println("");
        System.out.println("Adding new person into the list (after Bill)");
        people.add(1, new Person("Cpt. Morgan", 25));
        for (Person p : people) { System.out.println(p.toString()); }
        
             
        System.out.println("");
        System.out.println("Deleting the first person (Bye Bill)");
        people.deleteFirst();
        for (Person p : people) { System.out.println(p.toString()); }        
        
        System.out.println("");
        System.out.println("Deleting the last person (Bye Cpt. Crunch)");
        people.deleteLast();
        for (Person p : people) { System.out.println(p.toString()); }  
        
        
        
    }
    
    
    
    
}
