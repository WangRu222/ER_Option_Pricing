
# Black Scholes
The basic idea of ​​Black-Scholes option pricing is no-arbitrage pricing, assuming that option prices and stock prices are both affected by uncertain factors, and individual investment returns are uncertain. By managing a certain number of basic options and behavioral combinations, risks can be covered and uncertainties eliminated. Therefore, the differential equation of the Black-Scholes option pricing model is:

$$
\frac{\partial \mathrm{v}}{\partial t}+r S_t \frac{\partial v}{\partial S_t}+\frac{1}{2} \sigma^2 \frac{\partial^2 v}{\partial S_t^2}-r V=0
$$

Where, $S_t$ is the price of the underlying asset at time t, v is the price of the European option that depends on $S_t$, $R$ is the risk-free interest rate calculated by continuous compounding, $\sigma$ is the volatility of the underlying asset price, $T$ is the option expiration date, and $t$ is the current pricing date.

The pricing formulas for call options and put options are shown in equations 2.2 and 2.3 respectively:

$$
\begin{aligned}
& \mathrm{C}(\mathrm{~S}, \mathrm{~T})=\mathrm{SN}\left(\mathrm{~d}_1\right)-\mathrm{Ke}^{-r T} N\left(d_2\right) \\
& \mathrm{p}(\mathrm{~S}, \mathrm{~T})=\mathrm{Ke}^{-r T} N\left(-d_2\right)-S N\left(-d_1\right)
\end{aligned}
$$

Where, $C(S, T)$ is the price of the call option, $p(S, T)$ is the price of the put option, and $K$ is the exercise price of the option.

$$ \begin{gathered} \mathrm{d}_1=\frac{\ln \left(\frac{S}{K}\right)+\left(\propto_S+\sigma^2 / 2\right) T}{\sigma \sqrt{T}} \\ \mathrm{~d}_2=\mathrm{d}_1-\sigma \sqrt{T} \end{gathered} $$
# Monte Carlo
As mentioned above, the Monte Carlo simulation method needs to simulate the price path of the underlying asset, and the change of the price path is random, which can be modeled by mathematical random processes. Therefore, this section will introduce the mainstream random processes.

Roughly speaking, a random process is a sequence of random variables. However, the selection of random numbers is generally not independent, but depends on the results of the previous selections. However, the random processes used in finance usually exhibit Markov characteristics - the main meaning is that tomorrow's process value depends only on today's process state, not on any other "historical" state, or even on the entire path history. This process is also called a "memoryless process"
## Brown motion
$$
dS_t=rS_tdt+\sigma S_t~d Z_t
$$
## Heston
$$
dS=\mu Sd t+\sqrt{v} ~S d W_t^1 
$$

$$
dv_t=\kappa\left(\theta-v_t\right) d t+\delta \sqrt{v_t} d W_t^2
$$ 

## Merton

$$
 d S_t=\left(r-r_J\right) S_t d t+\sigma S_t d W_t+J S_t d P_t 
$$
 
$$
prob\left(d P_t=1\right)=\lambda_p d t
$$
# Binary Tree
The core idea of ​​the binomial model is to divide the option within the duration into many small time intervals, and assume that in each time interval the price of the underlying asset has only two possibilities: rising or falling. The probability of rising is $p$, and the probability of falling is 1 - $p$.
# Least Square Monte Carlo method 
Monte Carlo simulation is a flexible and powerful numerical method, but it is not suitable for solving the pricing problem of American options or Bermuda options. Scholars Longstaff and Schwarta proposed the Least-Squares Monte Carlo Simulation Method (LSM), which has become a classic method for pricing American options.
