# visualize_operators
Visualize various recombination and mutation operators for genetic algorithms.

<b>src:</b> 

- Includes python code for various mating and mutation operators. 

Code influenced by David Hadka and MOEAFramework (https://github.com/MOEAFramework) - translated into Python in two dimensions.

Polynomial Mutation (PM) operator: 
Deb, K. and Goyal, M. "A combined genetic adaptive search (GeneAS) for engineering design."
 * Computer Science and Informatics, 26(4):30-45, 1996.
 
Simulated Binary Crossover (SBX) operator: 
Deb, K. and Agrawal, R. B.  "Simulated Binary Crossover for Continuous
 *       Search Space."  Indian Institute of Technology, Kanpur, India.  
 *       Technical Report No. IITK/ME/SMD-94027, 1994.
 
Parent Centric Crossover (PCX) operator: 
Deb, K., Anand, A., and Joshi, D., "A Computationally Efficient Evolutionary Algorithm for
 * Real-Parameter Optimization," Evolutionary Computation, 10(4):371-395, 2002.
 
Simplex Crossover (SPX) operator:
Tsutsui, S., Yamamura, M., and Higuchi, T., "Multi-parent Recombination
 * with Simplex Crossover in Real Coded Genetic Algorithms," Proceedings of the
 * Genetic and Evolutionary Computation Conference, vol. 1, pp. 657-664, 1999.
Higuchi, T., Tsutsui, S., and Yamamura, M., "Theoretical Analysis of
 * Simplex Crossover for Real-Coded Genetic Algorithms," Parallel Problem
 * Solving from Nature PPSN VI, pp. 365-374, 2000.
 
Uniform Normaml Distribution (UNDX) operator:
Kita, H., Ono, I., and Kobayashi, S., "Multi-parental Extension of the Unimodal Normal
 * Distribution Crossover for Real-coded Genetic Algorithms," Proceedings of the 1999 Congress on
 * Evolutionary Computation, pp. 1581-1588, 1999.
Deb, K., Anand, A., and Joshi, D., "A Computationally Efficient Evolutionary Algorithm for
 * Real-Parameter Optimization," Evolutionary Computation, vol. 10, no. 4, pp. 371-395, 2002.
 
Uniform Mutation (UM) operator.

- Includes python script for plotting a monte-carlo sampling of each mating operator. Figure inspired by:

Hadka, D. and P. Reed. Borg: An Auto-Adaptive Many-Objective Evolutionary Computing Framework. 
Evolutionary Computation, 21(2):231-259, 2013.

- Includes webpage with D3.js code for interactive visualization of the effects of parameters on each operator.


data: 

- Includes .csv data for monte carlo sampling of each operator.

figures:

- Includes relevant images.
