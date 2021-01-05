%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% Description of variables in the DDK_Data File. The original data can %
%%% be obtained from the American Economic Review website %%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% NOTE: Missing observations have a value of NaN
% The following are the main variables
schoolid;                  % ID of the school, helpful for clustering
tracking;                  % Indicator for whether school is tracked
girl;                      % A dummy for whether student is a girl
agetest;                   % Age of the student
etpteacher                 % A dummy for whether the teacher was a contract teacher
lowstream;                 % A dummy for assigned to lower section in tracking school
bottomhalf;                % Dummy for bottom half of initial distribution
tophalf;                   % Dummy for top half of initial distribution
bottomquarter;             % Dummy for top half of initial distribution
secondquarter;             % Dummy for 2nd quarter of initial distribution
thirdquarter;              % Dummy for 3rd quarter of initial distribution
topquarter;                % Dummy for top quarter of initial distribution
std_mark;                  % Initial Test Score
percentile;                % The initial score in percentile
litscore;                  % Endline score in language (1st round)
mathscoreraw;              % Endline score in mathematics (1st round)
totalscore;                % Endline total score (1st round)

% Extract the variable names from big matrix - Second round variables
r2_age;                    % The age on the second round of interviews
r2_litscore;               % Endline score in language
r2_mathscoreraw;           % Endline score in mathematics
r2_totalscore;             % Endline total score




