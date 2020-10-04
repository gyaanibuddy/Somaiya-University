import java.util.*;
class Process {
  int pid; // process id
  int bt; //burst time
  int at; //arrival time

  Process(int pid,int bt,int at){
    this.pid = pid;
    this.bt = bt;
    this.at = at;
  }

}

class Main {

  static void filter(Process[] proc,int curr_process,int current_time,ArrayList<Integer> q,int[] rt){
    int n = proc.length;
    for(int i=0;i<n;i++){
      if(i!= curr_process && rt[i] > 0 && proc[i].at <= current_time  && q.indexOf(i) == -1){
        q.add(i);
      }
    }
  }
  

  static void sortByArrivalTime(Process[] proc){
    ArrayList<Process> arr = new ArrayList<Process>();
    for(int i=0;i<proc.length;i++) arr.add(proc[i]);
    Collections.sort(arr, new Comparator<Process>() {
        public int compare(Process p1,Process p2){
          return p1.at - p2.at;
        }
    });
  }

  static void findWaitingTimeAndTurnAroundTime(Process proc[],int n,int wt[],int tat[],int ct[]){
    sortByArrivalTime(proc);
    //remaining time
    int rt[] = new int[n];
    int quantum = 3;

    for(int i=0;i<n;i++) rt[i] = proc[i].bt;

    int process_completed = 0;
    int current_time = 0;

    ArrayList<Integer> q = new ArrayList<Integer>();

    // Get the first process and put it into queue
    q.add(0);
    current_time = proc[0].at;
    int curr_process = 0;

    System.out.print("ORDER:   ");
    while(process_completed != n){
      
      if(q.size() != 0){
        curr_process = q.get(0); //index
        System.out.print("P"+proc[curr_process].pid+"  ");
        q.remove(0);
        
        if(rt[curr_process] > quantum){
          rt[curr_process] -= quantum;
          current_time += quantum;

          //Now add all the process which have arrived during this time in the queue
          filter(proc,curr_process,current_time,q,rt);
          q.add(curr_process);
        }
        else{
          process_completed++;
          current_time += rt[curr_process];
          ct[curr_process] = current_time;
          tat[curr_process] = current_time - proc[curr_process].at;
          wt[curr_process] = tat[curr_process] - proc[curr_process].bt;
          rt[curr_process] = 0;

          //Now add all the process which have arrived during this time in the queue
         
          filter(proc,curr_process,current_time,q,rt);
        }
      }
      else{ //q is empty
        current_time++;
        curr_process = -1;
        filter(proc,curr_process,current_time,q,rt);
      }
    }
    System.out.print("\n\n");
    
  }

  static void printTable(int[] wt,int[] tat,int n,Process[] proc,int ct[]){
    int  total_wt = 0, total_tat = 0; 
    System.out.println("Processes " + " Burst time " + " Arraval time " + " Waiting time " + " Turn around time  "+"  current_time"); 
       
        // Calculate total waiting time and 
        // total turnaround time 
        for (int i = 0; i < n; i++) { 
            total_wt = total_wt + wt[i]; 
            total_tat = total_tat + tat[i]; 
            System.out.println(" " + proc[i].pid + "\t\t\t\t"+ proc[i].bt + "\t\t "+proc[i].at + "\t\t\t\t " + wt[i] + "\t\t\t\t\t" + tat[i]+"\t\t\t\t" + ct[i]); 
        } 
       
        System.out.println("Average waiting time = " + (float)total_wt / (float)n); 
        System.out.println("Average turn around time = " + (float)total_tat / (float)n); 
  }

  static void findAvgTime(Process proc[],int n){
    int wt[] = new int[n];
    int tat[] = new int[n];
    int ct[] = new int[n];

    findWaitingTimeAndTurnAroundTime(proc,n,wt,tat,ct);

    printTable(wt,tat,n,proc,ct);
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    Process proc[] = { 
      // new Process(pid,bt,at)
      
      // Having different arrival time
      new Process(1, 8, 0),  
      new Process(2, 2, 5), 
      new Process(3, 7, 1),  
      new Process(4, 3, 6),
      new Process(5, 5, 8)

      // Having same arrival time
      // new Process(1, 10, 0),  
      // new Process(2, 5, 0),  
      // new Process(3, 8, 0)  

    }; 
    findAvgTime(proc, proc.length);
  }
}