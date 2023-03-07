import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
// 1.Вычислить n-ое треугольного число(сумма чисел от 1 до n), а так же n! (произведение чисел от 1 до n)
// Ввод:5

// 1.1Треугольное число 1 + 2 + 3 + 4 + 5 = 15 
// public class HomeWork {

//     public static void main(String[] args) {
        
//         Scanner scanner = new Scanner(System.in);
//         int finish = scanner.nextInt();
//         scanner.close();
//         int summ = 0;
//         for (int i = 1; i <= finish; i++) {
//             summ += i;
//         }
//         System.out.println(summ);
//     }
// }

// 1.2n! 1 * 2 * 3 * 4 * 5 = 120
// public class HomeWork {
// public static void main(String[] args){
//     Scanner scanner = new Scanner(System.in);
//     int finish = scanner.nextInt();
//     scanner.close();
//     int result = 1;
//     for (int i = 1; i <= finish; i++){
//         result *= i;
//     }
//     System.out.println(result);
// }
// }




// 2.Вывести все простые числа от 1 до 1000
// public class HomeWork {
//     public static void main(String[] args) {
//         int n = 1000;

//         nextPrime:
//         for (int i = 2; i <= n; i++) {
        
//           for (int j = 2; j < i; j++){
//             if (i % j == 0) continue nextPrime;
//           }
//           System.out.println(i);
//         }
            
//     }
// }




// 3.Реализовать простой калькулятор (+ - / *)
// Ввод числа ->
// Ввод знака ->
// Ввод числа ->


public class HomeWork {
    public static void main(String[] args) {
       int num1;
       int num2;
       int ans;
       char op;
       Scanner reader = new Scanner(System.in);
       System.out.print("Введите 2 числа: ");
       num1 = reader.nextInt();
       num2 = reader.nextInt();
       System.out.print("\nВведите оператор (+, -, *, /): ");
       op = reader.next().charAt(0);
       reader.close();
       switch(op) {
          case '+': ans = num1 + num2;
             break;
          case '-': ans = num1 - num2;
             break;
          case '*': ans = num1 * num2;
             break;
          case '/': ans = num1 / num2;
             break;
          default:  System.out.printf("Ошибка");
             return;
       }
       System.out.printf(num1 + " " + op + " " + num2 + " = " + ans);
    }
 }