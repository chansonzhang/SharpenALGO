/**
 * Created by zhangchen on 2016/9/6.
 * Contact Me: chansonzhang@163.com
 */
public class Eratosthenes {
    public static void main(String[] args){
        int max=10000;
        int count=6;
        int[] numbers=new int[max+1];
        boolean[] exists=new boolean[max+1];
        for(int i=0;i<max+1;i++){
            numbers[i]=i;
            exists[i]=true;
        }
        eratosthenes(numbers,exists,max,count);
        for(int i=0;i<numbers.length;i++){
            if(exists[i]){
                System.out.print(numbers[i]+" ");
            }
        }
    }

    public static void eratosthenes(int[] numbers,boolean[] exists,int max,int count) {
        for (int i = 0; i < count; i++) {
            if (i == 0) {//先删除所有偶数
                for (int j = 0; j < max + 1; j += 2) {
                    exists[j] = false;
                }
            } else {
                int a;
                int index = 0;
                int c = 0;
                while (c != i + 1) { //找出第i+1个未被划去的数字
                    if (exists[index++]) {
                        c++;
                    }
                }
                a = numbers[index - 1];

                //找到第a个true的索引
                index = 0;
                c = 0;
                while (c != a) {
                    if (exists[index++]) {
                        c++;
                    }
                }

                //此时c=a,index对应第a个true的索引
                while (index < max + 1) {
                    if (c % a == 0) { //删除所有第na个true
                        exists[index - 1] = false;
                    }
                    if (exists[index]) {
                        c++;
                    }
                    index++;
                }
            }
        }
    }
}
