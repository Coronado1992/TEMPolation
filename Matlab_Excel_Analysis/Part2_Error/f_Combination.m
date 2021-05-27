function [ncombinations,combinations] = f_Combination(numDP,missing_data)

ncombinations = factorial(numDP)/(factorial(missing_data)*factorial(numDP-missing_data));
combinations = nchoosek (1:numDP,missing_data);
ncombinations = round(ncombinations);
end

