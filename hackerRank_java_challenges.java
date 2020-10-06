
// HashSets


//Write your code here
    HashSet<String> hs = new HashSet<String>();
    for(int i=0; i< t; i++){
        hs.add(pair_left[i]+"_"+pair_right[i]);
        System.out.println(hs.size());
    }

//HashMap


class Solution{
	public static void main(String []argh)
	{
        HashMap<String, Integer> hm = new HashMap<>();
		Scanner in = new Scanner(System.in);
		int n=in.nextInt();
		in.nextLine();
		for(int i=0;i<n;i++)
		{
			String name=in.nextLine();
			int phone=in.nextInt();
			in.nextLine();

            hm.put(name, phone);
		}
		while(in.hasNext())
		{
			String s=in.nextLine();
            try{
                int phoneNumber = hm.get(s);
                System.out.println(s+"="+phoneNumber);
            }
            catch(Exception e){
                System.out.println("Not found");
            }
		}
	}
}


/// deque

    // deque

public int deque() {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        HashMap<Integer, LinkedList<Integer>> hs = new HashMap<Integer, LinkedList<Integer>>();

        int runningSize = 0;
        int x;
        int k = 0;
        int maxSize = 0;
        for (int i = 0; i < n; i++) {
            int num = in.nextInt();
            try{
                LinkedList<Integer> temp = hs.get(num);
                if(temp.size() > 0){
                    x = temp.removeFirst();
                    k = x + 1;
                    maxSize = Math.max(runningSize, maxSize);
                    runningSize = i-k+1;
                }
            }
            catch(Exception e){
                LinkedList<Integer> temp = new LinkedList<Integer>();
                temp.add(i);
                hs.put(num, temp);
                runningSize++;;
            }

        }//outer for
        System.out.println(Math.max(maxSize,runningSize));
        return maxSize;
    }

