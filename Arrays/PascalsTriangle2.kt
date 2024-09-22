//https://leetcode.com/problems/pascals-triangle-ii/description/
fun main() {
    val rowIndex = 5
    val result = getRow(rowIndex)
    println(result)
}

fun getRow(rowIndex: Int): List<Int> {
    
    var outputList: MutableList<Int> = ArrayList()
    outputList.add(1)
    if(rowIndex == 0){
        return outputList
    }
    outputList.add(1)
    if(rowIndex == 1){
        return outputList
    }

    for(i in 0 until rowIndex-1){
        var temp: MutableList<Int> = ArrayList()
        temp.add(0,1)

        for(j in 1 until outputList.size){
            temp.add(j,outputList[j]+outputList[j-1])
        }
        temp.add(1)
        outputList = temp
    }

    return outputList;
}
