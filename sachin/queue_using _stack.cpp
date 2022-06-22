#include<bits/stdc++.h>
using namespace std;

class Queue{
    public:
    stack<int> s;

    void push(int val){
        stack<int> s2;
        while(!s.empty()){
            int temp = s.top();
            s.pop();
            s2.push(temp);
        }
        s.push(val);
        while(!s2.empty()){
            int temp = s2.top();
            s2.pop();
            s.push(temp);
        }
    }

    int pop(){
        int temp = s.top();
        s.pop();
        return temp;
    }

    int top(){
        return s.top();
    }
};



class Queue2{
    public:
    stack<int> input;
    stack<int> output;

    void push(int val){
        input.push(val);
    }

    int pop(){
        int temp =0;
        if(!output.empty()){
            temp = output.top();
            output.pop();
        }
        else{
            while(!input.empty()){
                output.push(input.top());
                input.pop();
            }
            temp = output.top();
            output.pop();
        }
        return temp;

    }
};


int main(){
    Queue2 q1 = Queue2();
    q1.push(2);
    q1.push(3);
    q1.push(9);
    q1.push(4);
    cout<<q1.pop()<<endl;
    // cout<<q1.top()<<endl;
    cout<<q1.pop()<<endl;
    return 0;
}