<h3>Print all Permutations of a String/Array</h3>

<p>We will not be using extra map/data structure to store the permutation
rather we will USE SWAP to generate all permutation</p>

<ol>
    <li>Intially You have 3 options to SWAP with</li>
    <li>We start at Index 0</li>
    <li>SWAP index 0 with index 0 which is 1 with 1</li>
    <li>SWAP index 0 with index 1 which is 1 with 2 </li>
    <li>SWAP index 0 with index 3 which is 1 with 3 </li>
    <li>Once you Swap with index 0 and the pointer goes out the LIST you get the permutation</li>
</ol>