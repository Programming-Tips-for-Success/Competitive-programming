Algorithm(x, k)
y ← x
while y!=nil do
 if key[y] = k then return y
 else if key[y] < k then y ← right[y]
 else y ← left[y]

 return (“NOT FOUND”)
 
 function(int n)
{
    if(n == 1) return;

    for(i = 1 ; i <= n ; i++)
        for(j = 1 ; j <= n ; j++)
            printf("*");

    function(n-1);
}

function foo(n)
{
    if(n == 1) return;

    for(let i = 1 ; i <= n ; i++)
        for(let j = 1 ; j <= n ; j++)
            console.log('*');

    foo(n-1);
}

SORT (A)
{
 n ← length [A]
  For i = 1 to n do
 Insert A[i] into list B[A[i]/b] ..(b<- constant)
  For i = 0 to n-1 do
  Sort list B with Insertion sort
 
 Concatenate the lists B[0], B[1], . . B[n-1]..
}

