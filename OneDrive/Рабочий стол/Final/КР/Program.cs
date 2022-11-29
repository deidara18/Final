
string[] array1 = new string[5] {"dotnet", "123", "qwerty", "zxc", "Hello"};
string[] array2 = new string[array1.Length];

Sort(array1, array2);
PrintArray(array1);
Console.WriteLine("--------");
PrintArray(array2);

void Sort (string[] array1, string[] array2){
    int temp = 0;
    for(int i = 0; i < array1.Length; i++){
        if (array1[i].Length <= 3){
            array2[temp] = array1[i];
            temp++; 
        }
    } 
}

void PrintArray(string[] Array){
    for(int i = 0; i < Array.Length; i++){      
            Console.Write($"{Array[i]} ");
        Console.WriteLine();
    }
}
