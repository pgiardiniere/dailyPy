public class Urlify_1_3 {

    public static void main(String[] args) {
        char[] arr = { 'o','n','e',' ','s','p','a','c','e' };
        
        System.out.println(arr);

        int i = 0;
        int count = 0;
        for (char c : arr) {
            if (c == ' ')
                count++;
        }

        System.out.println(arr);
        System.out.println(count);
    }
}