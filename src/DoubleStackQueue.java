import java.util.Stack;

/**
 * Copyright 2018 Zhang, Chen. All Rights Reserved.
 * <p>
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * <p>
 * http://www.apache.org/licenses/LICENSE-2.0
 * <p>
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * ==============================================================================
 *
 * @Time : 12/24/2018 21:38
 * @Author : Zhang, Chen (chansonzhang)
 * @Email : ZhangChen.Shaanxi@gmail.com
 * @FileName: DoubleStackQueue.java
 */
public class DoubleStackQueue<T> {
    private Stack<T> stackIn;
    private Stack<T> stackOut;

    public DoubleStackQueue(){
        stackIn=new Stack<>();
        stackOut=new Stack<>();
    }

    public T push(T x){
        stackIn.push(x);
        return x;
    }

    public T pop(){
        shiftStack();
        return stackOut.pop();
    }

    public boolean isEmpty(){
        return 0==stackIn.size() && 0==stackOut.size();
    }

    private void shiftStack(){
        if(stackOut.empty()) {
            while (!stackIn.isEmpty()) {
                stackOut.push(stackIn.pop());
            }
        }
    }

    public static void main(String[] args){
        DoubleStackQueue<Integer> myQueue=new DoubleStackQueue<>();
        for(int i=0;i<10;i++){
            myQueue.push(i);
        }
        while (!myQueue.isEmpty()){
            System.out.print(myQueue.pop()+" ");
        }

        System.out.println();
        myQueue.push(0);
        myQueue.push(1);
        myQueue.push(2);
        System.out.print(myQueue.pop()+" ");
        myQueue.push(3);
        myQueue.push(4);
        myQueue.push(5);

        while (!myQueue.isEmpty()){
            System.out.print(myQueue.pop()+" ");
        }
    }
}
