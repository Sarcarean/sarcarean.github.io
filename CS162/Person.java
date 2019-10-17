public class Person
{
    private String my_name;
    private int my_age;

    public Person(String name, int age)
    {
        this.my_name = name;
        this.my_age = age;
    }

    public String getName() 
    {
        return my_name;
    }
    
    public int getAge()
    {
        return my_age;
    }
        
    public String toString()
    { 
        return this.my_name + " (" + this.my_age + " years old)";   
    }
    
}
