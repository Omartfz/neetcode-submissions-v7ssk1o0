class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> counts;
        for (int i=0;i< nums.size();i++){
            counts[nums[i]]++;
            if (counts[nums[i]]>1) return true;
        }
    return false;
    }
};