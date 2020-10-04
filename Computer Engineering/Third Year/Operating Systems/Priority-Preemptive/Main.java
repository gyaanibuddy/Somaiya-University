import java.util.*;
class Process {
  int pid; // process id
  int bt; //burst time
  int at; //arrival time
  int priority;

  Process(int pid,int bt,int at,int priority){
    this.pid = pid;
    this.bt = bt;
    this.at = at;
    this.priority = priority;
  }

}

class Main {

  static void findWaitingTimeAndTurnAroundTime(Process proc[],int n,int wt[],int tat[]){
    //remaining time
    int rt[] = new int[n];

    for(int i=0;i<n;i++) rt[i] = proc[i].bt;

    int process_completed = 0;
    int current_time = 0;
    System.out.println();
    while(process_completed != n){
     
      int shortest = -1;
      int minn = Integer.MAX_VALUE; // this is minn priority
      for(int i=0;i<n;i++){
        if((proc[i].at <= current_time) && proc[i].priority < minn && rt[i] > 0){
          minn = proc[i].priority;
          shortest = i;
        }
      }
      

      // If no process satisfies all conditions
      if(shortest == -1){
        current_time++;
        continue;
      }

      System.out.print("P"+proc[shortest].pid+"  ");

      // If process is found which satifies the conditions
      rt[shortest]--;
      current_time++;

      // If time left for this process is 0 then increment process_completed
      if(rt[shortest] == 0){
        process_completed++;
        int finish_time = current_time;
        // System.out.println("P "+(shortest+1)+"   CT:"+finish_time+"  AT:"+proc[shortest].at);
        tat[shortest] = finish_time - proc[shortest].at;
        wt[shortest] = tat[shortest] - proc[shortest].bt;
      }


    }
    
  }

  static void printTable(int[] wt,int[] tat,int n,Process[] proc){
    int  total_wt = 0, total_tat = 0; 
    System.out.println();
    System.out.println("Processes "+ " Arrival time " + " Burst time " + " Waiting time " + " Turn around time"); 
       
        // Calculate total waiting time and 
        // total turnaround time 
        for (int i = 0; i < n; i++) { 
            total_wt = total_wt + wt[i]; 
            total_tat = total_tat + tat[i]; 
            System.out.println(" " + proc[i].pid + "\t\t\t\t"+ proc[i].at +"\t\t\t"+ proc[i].bt + "\t\t\t\t " + wt[i] + "\t\t\t\t" + tat[i]); 
        } 
       
        System.out.println("Average waiting time = " + (float)total_wt / (float)n); 
        System.out.println("Average turn around time = " + (float)total_tat / (float)n); 
  }

  static void findAvgTime(Process proc[],int n){
    int wt[] = new int[n];
    int tat[] = new int[n];

    findWaitingTimeAndTurnAroundTime(proc,n,wt,tat);

    printTable(wt,tat,n,proc);
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    System.out.println("Enter the number of processes :");
    int n = sc.nextInt();
    Process[] proc = new Process[n];
    for(int i=0;i<n;i++){
      System.out.println("Enter process id, burst time, arrival time, priority for process "+(i+1));
      //int pid,int bt,int at,int priority
      proc[i] = new Process(sc.nextInt(),sc.nextInt(),sc.nextInt(),sc.nextInt());
    }

    
    // Process proc[] = { 
    //   //int pid,int bt,int at,int priority
    //   new Process(1, 8, 0, 3),  
    //   new Process(2, 2, 1, 4), 
    //   new Process(3, 4, 3, 4),  
    //   new Process(4, 1, 4, 5),
    //   new Process(5, 6, 5, 2),
    //   new Process(6, 5, 6, 6),
    //   new Process(7, 1, 10, 1),
    // }; 
    findAvgTime(proc, proc.length);
  }
}