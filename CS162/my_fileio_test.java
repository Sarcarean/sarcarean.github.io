import java.io.*;
import java.util.*;

public class my_fileio_test
{
    private static final String input_file = "test_file_in.txt";
    private static final String output_file = "test_file_out.txt";
    
    public static void main(String args[]) 
    { 
        DLinkedList<Integer> my_int_list = new DLinkedList<>();
        BufferedReader reader = null;
        try {
            reader = new BufferedReader(new FileReader(input_file));
            String line = reader.readLine();
            while (line != null) {
                Integer n = new Integer(Integer.parseInt(line.trim()));
                my_int_list.addLast(n);
                line = reader.readLine();
            }
        } catch(IOException e) {
              System.out.println("ERROR: Unable to open file for reading");
              return;
        } finally {
            try {
                if (reader!=null) { reader.close(); }
            } catch(IOException e) {
            }
        }
        System.out.println("Pre-sorted list of random numbers from a text file:");
        for (Integer x : my_int_list) { System.out.println(x.toString()); }
        
        List<Integer> l = new ArrayList<>();
        for (Integer x : my_int_list) { l.add(x); }
        Collections.sort(l);
        
        System.out.println("Sorted list:");
        for (Integer x : l) { System.out.println(x.toString()); }       
        
        BufferedWriter writer = null;
        try {
            writer = new BufferedWriter(new FileWriter(output_file));
            for (int i = 0; i < l.size(); i++) {
                 writer.write(Integer.toString(l.get(i)));
                 writer.newLine();
            }
            writer.flush();  
        } catch(IOException e) {
              System.out.println("ERROR: Unable to open file for writing");
              return;
        } finally {
            try {
                if (reader!=null) { writer.close(); }
            } catch(IOException e) {
            }
        }               
        System.out.println("Sorted list saved successfully!");
    }
}
