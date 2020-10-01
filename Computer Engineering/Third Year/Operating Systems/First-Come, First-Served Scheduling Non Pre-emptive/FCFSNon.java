// To implement basic Non –Pre-emptive Process management algorithm Priority Scheduling

// First Come, First serve

import java.lang.*;
import java.util.*;
class FCFSNon {

  public static int sum(int i,int process_burst_time[])
  {
    int ans = 0;
    for(int k = 0;k<i;k++)
    {
      ans = ans + process_burst_time[k];
    }
    return ans;
  }

  public static void main(String[] args) {
    System.out.println("Enter the process ids and burst time for the process :");
    System.out.println("Enter number of process");
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int process[] = new int[n];
    int process_waiting_time[] = new int[n];
    int process_turnaround_time[] = new int[n];
    int process_burst_time[] = new int[n];
    for(int i = 0; i<n; i++)
    {
    process[i] = sc.nextInt();
    }

    for(int i = 0; i<n; i++)
    {
    process_burst_time[i] = sc.nextInt();
    }

    for(int i = 0; i<n; i++)
    {
    System.out.println(process[i] + " " + process_burst_time[i]);
    }

    process_waiting_time[0] = 0;
    process_turnaround_time[0] = process_burst_time[0];
    for(int i = 1; i<n; i++)
    {
      process_waiting_time[i] = sum(i, process_burst_time);
      process_turnaround_time[i] = sum(i+1, process_burst_time);
    }
    System.out.println("\n");
    float sum1 = 0, sum2 = 0;
    System.out.println("process ID" + "\t" + "burst_time" + "\t" +  "waiting_time" + "\t" + "turnaround_time");
    for(int i = 0; i<n; i++)
    {
    System.out.println(process[i] + "\t\t\t" + process_burst_time[i] + "\t\t\t" +  process_waiting_time[i] + "\t\t\t\t" + process_turnaround_time[i]);
    sum1 = sum1 + process_waiting_time[i];
    sum2 = sum2 + process_turnaround_time[i];
    }
    float avg1 = sum1/n;
    float avg2 = sum2/n;  

    System.out.println("\nAverage waiting time : "+avg1);
    System.out.println("\nAverage turnaround time : "+avg2);
   }
}
