class Solution 
{
public:
    bool isValid(string s) 
    {
        stack<char> CharStack;

        for(char c:s)
        {
            if (c=='(' || c=='{' || c=='[')
            {
                CharStack.push(c);
            }
            else
            {
                if (CharStack.empty())
                {
                    return false;
                }

                char top=CharStack.top();
                CharStack.pop();

                if(   c==')' && top!='('
                   || c=='}' && top!='{'
                   || c==']' && top!='[' )
                {
                    return false;
                }
            }
        }

        return CharStack.empty();
    }
};