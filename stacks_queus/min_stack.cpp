class MinStack {
    private:
        stack<int> original;
        stack<int> minstack;
    public:
        MinStack();
        void push(int x);
        void pop();
        int top();
        int getMin();
};

MinStack::MinStack() {
}

void MinStack::push(int x) {
    original.push(x);
    if(minstack.empty() || x <= minstack.top())
        minstack.push(x);
}

void MinStack::pop() {
    if(minstack.top() == original.top())
        minstack.pop();
    original.pop();
}

int MinStack::top() {
    if(original.empty())
        return -1;
    return original.top();
}

int MinStack::getMin() {
    if(minstack.empty())
        return -1;
    return minstack.top();
}