
/**
 * Copyright 2021 Zhang, Chen. All Rights Reserved.
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
 * @author Zhang Chen(ChansonZhang)
 * @since 2021/7/21 20:15
 */
public class LinkedListUtils {
    public static void main(String[] args) {

        Node<Integer> head = new Node<>(null);
        Node<Integer> current = head;
        for (int i = 0; i < 10; i++) {
            Node<Integer> node = new Node<>(i);
            current.setNext(node);
            current = node;
        }

        print(head);

        reverse(head);

        print(head);

        reverseRecursiveWithHead(head);

        print(head);
    }

    public static void reverse(Node<Integer> head){
        Node<Integer> prev = null;

        //current point to first
        Node<Integer> current = head.getNext();

        Node<Integer> next;
        while (current != null) {
            //save next
            next = current.getNext();

            current.setNext(prev);

            prev = current;
            current = next;
        }
        //current is null, prev is the new first
        head.setNext(prev);
    }

    private static void reverseRecursiveWithHead(Node<Integer> head) {
        Node<Integer> first = head.getNext();
        Node<Integer> newFirst = reverseRecursive(first);
        head.setNext(newFirst);
        first.setNext(null);
    }

    public static Node<Integer> reverseRecursive(Node<Integer> first){
        Node<Integer> extra = first.getNext();
        if (extra != null) {
            Node<Integer> extraFirst = reverseRecursive(extra);
            extra.setNext(first);
            return extraFirst;
        }
        return first;
    }

    public static void print(Node<Integer> head) {
        Node<Integer> current = head;
        while (current.getNext() != null) {
            current = current.getNext();
            System.out.print(current.getData() + " ");
        }
        System.out.println();
    }
}


