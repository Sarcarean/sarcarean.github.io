import static org.junit.Assert.*;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;


public class my_unit_test
{

    DLinkedList<Person> people;
    
    public my_unit_test()
    {
    
    }

    @Before
    public void setUp()
    {
        people = new DLinkedList<>();
        people.addLast(new Person("Bill Gates", 55));
        people.addLast(new Person("Steve Jobs", 35));
        people.addLast(new Person("Elon Musk", 42));
        people.addLast(new Person("Charlie Day", 25));
        people.addLast(new Person("Cpt. Crunch", 15));        
    }

    @After
    public void tearDown()
    {
        
    }

    @Test
    public void testCount()
    {
        assertEquals("Result",people.size(),5);
    }
    
    @Test
    public void removePerson() //Removes a person and checks to see that it did
    {     
        Person this_guy = (Person)people.get(1);
        boolean contains_steve = false;
        people.delete(1);   //Index for Steve Jobs
        for (Person p : people) { 
            if (p.getName().equals(this_guy.getName())) { contains_steve = true; }
        }
        assertEquals("Result",contains_steve,false);
    }
    
    @Test
    public void removeFirstPerson()
    {
        Person this_guy = (Person)people.get(0); //Index for Bill Gates
        boolean contains_bill = false;
        people.deleteFirst();
        for (Person p : people) { 
            if (p.getName().equals(this_guy.getName())) { contains_bill = true; }
        }
        assertEquals("Result",contains_bill,false);        
    }
    
    @Test
    public void removeLastPerson()
    {
        Person this_guy = (Person)people.get(4); //Index for Cpt. Crunch
        boolean contains_bill = false;
        people.deleteLast();
        for (Person p : people) { 
            if (p.getName().equals(this_guy.getName())) { contains_bill = true; }
        }
        assertEquals("Result",contains_bill,false);        
    }    
    
    @Test
    public void addAt() //Tests the insert/add at function of the list
    {
        String new_guy_name = "Cpt. Morgan";
        people.add(1, new Person(new_guy_name, 25));
        boolean contains_new_guy = false;
        for (Person p : people) { 
            if (p.getName().equals(new_guy_name)) { contains_new_guy = true; }
        }
        assertEquals("Result",contains_new_guy,true);    
        
    } 
    
}
