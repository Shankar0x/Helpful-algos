#include <stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    int arr[n][n];
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            scanf("%d",&arr[i][j]);
        }
    }
    int temp;
    for(int i=0;i<n/2;i++)
    {
        int l=n-i-1;
        for(int j=0;j<l-i;j++)
        {
            temp=arr[i][i+j];
            arr[i][i+j]=arr[l-j][i];
            arr[l-j][i]=arr[l][l-j];
            arr[l][l-j]=arr[i+j][l];
            arr[i+j][l]=temp;
        }
    }
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            printf("%d  ",arr[i][j]);
        }
        printf("\n");
    }
    return 0;
}
