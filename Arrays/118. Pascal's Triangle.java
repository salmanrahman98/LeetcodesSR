//https://leetcode.com/problems/pascals-triangle/

package Arrays;
import java.util.ArrayList;
import java.util.List;


class PascalTriangle1 {

    public static void main(String[] args) {
        int numRows = 20;
        List<List<Integer>> result = generate(numRows);
        for (List<Integer> row : result) {
            System.out.println(row);
        }
    }

    public static List<List<Integer>> generate(int numRows) {

        List<List<Integer>> outerList = new ArrayList<List<Integer>>();

        List<Integer> innerList = new ArrayList<Integer>();
        innerList.add(1);
        outerList.add(innerList);

        if(numRows == 1){
            return outerList;
        }
        innerList = new ArrayList<Integer>();
        innerList.add(1);
        innerList.add(1);
        outerList.add(innerList);

        List<Integer> temp = new ArrayList<Integer>();

        for(int i = 1 ; i < numRows-1;i++){
            innerList = outerList.get(i);
            temp = new ArrayList<Integer>();
            temp.add(0,1);

            for(int j = 1;j<innerList.size(); j++){
                temp.add(j,innerList.get(j) + innerList.get(j-1));
            }

            temp.add(1);
            outerList.add(temp);
        }

        return outerList;
    }
}