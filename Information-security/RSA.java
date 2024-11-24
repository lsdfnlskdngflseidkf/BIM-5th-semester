import java.util.Scanner;
public class RSA {
boolean testGCD(int a, int b){
    int r =a%b;
    while(r!=0){
        a=b;
        b=r;
        r=a%b;
    }
    if(b==1){
        return true;
    }
    else{
         return false;
    }
}
int multiInverse(int a, int n){
    for(int i=1;;i++){
        if(a*i%n==1){
            return i;
        }
    }
} 
int calcluateCipher(int m,int e, int n){
    int r=1;
    for(int i=1;i<=e;i++)
    {
        r=r*m%n;
        }
    return r;
    }


public static void main(String[] args)
{
    RSA obj=new RSA();
    Scanner sc=new Scanner(System.in);
    System.out.println("Enter two large prime numbers:");
    int p=sc.nextInt();
    int q=sc.nextInt();
    int n=p*q;
    int tn=(p-1)*(q-1);
    int e;
    do {
        System.out.println("Enter the value of e");
       e=sc.nextInt();
    }while(!(obj.testGCD(tn, e)&& e<tn && e>1));
    int d=obj.multiInverse(e, tn);
    System.out.println("n:"+n+"\ne:"+e+"\nd:"+d+"\ntn:"+tn);
    System.out.println("Enter the Plaintext:");
    int m=sc.nextInt();
    int c=obj.calcluateCipher(m,e,n);
    System.out.println("The Ciphertext is:"+c);
    int D=obj.calcluateCipher(c,d,n);
    System.out.println("The decrypted plaintext is:"+D);
    sc.close();
}
}
