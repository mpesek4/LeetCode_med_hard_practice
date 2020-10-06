// https://leetcode.com/problems/complement-of-base-10-integer/

// doing all easy problems and some mediums in java for a while
public int bitwiseComplement(int N) {
        String s = Integer.toString(N,2);
        StringBuilder sb = new StringBuilder();

        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == '0'){
                sb.append(1);
            }
            else {
                sb.append(0);
            }
        }
        String answer = sb.toString();
        return Integer.parseInt(answer,2);
    }



