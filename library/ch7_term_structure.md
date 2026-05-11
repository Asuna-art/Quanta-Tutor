# 第7章 利率期限结构

Chapter 7

Term Structure of Interest Rates
and Immunization

7.1     Overview
So far, it has generally been assumed that the interest rate i or force of interest δ
earned on an investment are independent of the term of that investment. In practice
the interest rate offered on investments does usually vary according to the term of the
investment. This is commonly referred to as the term structure of interest rates and
is often important to take this variation into consideration.
   In this chapter we will first consider how to deal with the term structure of interest
rates. We will mainly focus on fixed interest securities. We will then discuss how to
protect a fund against small movements of interest rates - the immunization of a fund.

   • The n-year spot rate, yn , is the annual interest rate that applies from the present
      time for the next n years. This is in contrast to the forward rate, ft,r , which
      applies over an r-year period starting at some future time t.

   • The n-year par yield is the annual coupon rate required for an n-year fixed
      interest security to be redeemed at par under the prevailing term structure.

   • The term structure of interest rates indicates how the spot rates available on
      investments are distributed with term. The structure can be explained by the
      interplay of liquidity preference theory, expectations theory, and market seg-
      mentation theory.

   • The discounted mean term (or Macauley duration) of a fixed-interest investment
      is the weighted average of the future times at which there are cash flows. The
      ‘weight’ associated with any given time is the present value of the net cash flow
      due at that time.
7.2 Term structure of interest rates                                                    90


       • The effective duration indicates the sensitivity of the present value of a cash
         flow to changes in the underlying rate of interest.

       • It is possible to immunize a fund to small changes in interest rate using the
         theory developed by Redington.


7.2         Term structure of interest rates
In investigating this variation, we make use of unit zero coupon bond prices. A
unit zero coupon bond of term n, say, is an agreement to pay £1 at the end of n years.
No coupon payments are paid. It is also called a pure discount bond.
       We denote the price at issue of a unit zero coupon bond maturing in n years by
Pn .


7.2.1        Discrete time
Discrete time spot rates

The yield on a unit zero coupon bond with term n years, yn , is called the n-year
spot rate of interest. Using the equation of value for the zero coupon bond we find
the yield on the bond yn from:

                                         1                       −n1
                              Pn =              ⇒ (1 + y n ) = P n
                                     (1 + yn )n
       Since rates of interest differ according to the term of the investment, in general
ys ̸= yt for s ̸= t. Every fixed-interest investment may be regarded as a combination
of (perhaps notional) zero coupon bonds. For example, a bond paying coupons of
D every year for n years, with a final redemption payment of R at time n may be
regarded as a combined investment of n zero coupon bonds with maturity value D,
with terms of 1 year, 2 years ..., n years, plus a zero coupon bond of nominal value R
with term n years.
       Defining vyt = (1 + yt )−1 , the price of the bond is:

                             A = D (P1 + P2 + · · · + Pn ) + RPn
                             A = D vy1 + vy22 + · · · + vynn + Rvynn
                                                            

       This is actually a consequence of ’no arbitrage’; the portfolio of zero coupon bonds
has the same payouts as the fixed-interest bond, and the prices must therefore be the
same.
       The variation by term of interest rates is often referred to as the term structure
of interest rates. The curve of spot rates {yt } is an example of a yield curve.
7.2 Term structure of interest rates                                                      91


Discrete time forward rates

The discrete time forward rate, ft,r , is the annual interest rate agreed at time 0 for
an investment made at time t > 0 for a period of r years.
   That is, if an investor agrees at time 0 to invest £100 at time t for r years, the
accumulated investment at time t + r is:


                                           100 (1 + ft,r )r

   Forward rates, spot rates and zero-coupon bond prices are all connected. The
accumulation at time t of an investment of 1 at time 0 is (1 + yt )t . If we agree at time
0 to invest the amount (1 + yt )t at time t for r years, we will earn an annual rate of fti .
So we know that £1 invested for t+r years will accumulate to (1 + yt )t (1 + ft,r )r . But
we also know from the (t + r) spot rates that £1 invested for t + r years accumulates
to (1 + yt+r )t+r , and we also know from the zero coupon bond prices that £1 invested
                                 −1
for t + i years accumulates to Pt+r .
   Hence, we know that:


                       (1 + yt )t (1 + ft,r )r = (1 + yt+r )t+r = Pt+r
                                                                    −1


   from which we find that:

                                       r  (1 + yt+r )t+r    Pt
                            (1 + ft,r ) =            t   =
                                            (1 + yt )      Pt+r
   so that the full-term structure may be determined given the spot rates, the forward
rates or the zero coupon bond prices.
   One-period forward rates are of particular interest. The one-period forward rate
at time t (agreed at time 0 ) is denoted ft = ft,1 . We define f0 = y1 . Comparing an
amount of f 1 invested for t years at the spot rate yt , and the same investment invested
1 year at a time with proceeds reinvested at the appropriate one-year forward rate,
we have:


                   (1 + yt )t = (1 + f0 ) (1 + f1 ) (1 + f2 ) . . . (1 + ft−1 )


7.2.2      Continuous time rates*
Continuous time spot rates

Let Pt be the price of a unit zero coupon bond of term t. Then the t-year spot force
of interest is Yt where:


7.2 Term structure of interest rates                                                   92



                                Pt = e−Yt t ⇒ Yt = − log Pt
                                                    t
   Arbitrage is the existence of risk-free profits. This is discussed in great detail
in CM2. This is also called the continuously compounded spot rate of interest or
the continuous-time spot rate. Yt and its corresponding discrete annual rate yt are
connected in the same way as δ and i; an investment of £1 for t years at a discrete
spot rate yt accumulates to (1 + yt )t ; at the continuous time rate it accumulates to
eyt t ; these must be equal, so:


                                          Y t = e Yt − 1

Continuous time forward rates

The continuous time forward rate Ft,r is the force of interest equivalent to the annual
forward rate of interest ft,r
   A £1 investment of duration r years, starting at time t, agreed at time 0 ≤ t
accumulates using the annual forward rate of interest to (1 + ft,r )r at time t + r.
   Using the equivalent forward force of interest, the same investment accumulates
to eFt,r r . Hence the annual rate and continuous-time rate are related as:


                                         ft,r = eFt,r − 1

   The relationship between the continuous time spot and forward rates may be
derived by considering the accumulation of £1 at a continuous time spot rate of Yt
for t years, followed by the continuous time forward rate of Ft,r for r years. Compare
this with an investment of £1 at a continuous time spot rate of Yt+r for t + r years.
   The two investments are equivalent, so the accumulated values must be the same.
Hence:

                                     etYt erFt,r = e(t+r)Yt+r
                                   ⇒tYt + rFt,r = (t + r)Yt+r
                                             (t + r)Yt+r − tYt
                                   ⇒Ft,r =
                                                     r
   Also, using Yt = − 1t log Pt , we have:
                                                              
                                            1            Pt
                                      Ft,r = log
                                            r           Pt+r

Instantaneous forward rates

The instantaneous forward rate Ft is defined as:
7.3 Theories of the term structure of interest rates                                 93



                                     Ft = lim Ft,r
                                           r→0

   The instantaneous forward rate may broadly be thought of as the forward force of
interest applying in the instant of time t → t + ∆t.
                                                   
                                       1        Pt
                             Ft = lim log
                                  r→0 r        Pt+r
                                         log Pt+r − log Pt
                                = − lim
                                    r→0          r
                                     d
                                = − log Pt
                                    dt
                                     1 d
                                =−        Pt
                                    Pt dt
   We also find, by integrating − dtd log Pt with Ft and using the fact that P0 = 1 (as
the price of a unit zero coupon bond of term zero years must be 1), that:

                                             Rt
                                     Pt = e− 0 Fs ds

   Note that we have described in this unit the initial term structure, where
everything is fixed at time 0 . In practice the term structure varies rapidly over time,
and the 5-year spot rate tomorrow may be quite different from the 5-year spot rate
today. In more sophisticated treatments we model the change in term structure over
time. In this case all the variables we have used, r.e.

                                 Pt yt ft,r Yt Ft,r

need another argument, v, say, to give the ’starting point’.
   For example, yv,t would be the t-year discrete spot rate of interest applying at
time v; Fv,t,r would be the force of interest agreed at time v, applying to an amount
invested at time v + t for the r-year period to time v + t + r.


7.3      Theories of the term structure of interest rates
7.3.1     Introduction
Some examples of typical (spot rate) yield curves are given below.




7.3 Theories of the term structure of interest rates                                 94




Figure 7.3.1 (a): Decreasing yield curve


   In Figure 7.3.1 (a), the long-term bond yields are lower than the short-term bonds.
Since price is a decreasing function of yield, an interpretation is that long-term bonds
are more expensive than short-term bonds.
   There are several possible explanations - for example, it is possible that investors
believe that they will get a higher overall return from long-term bonds, despite the
lower current yields, and the higher demand for long-term bonds has pushed up the
price, which is equivalent to pushing down the yield, compared with short-term bonds.
   Other explanations for different yield curve shapes are given below.




Figure 7.3.1 (b): Euro Area Yield Curves for all bonds
   In Figure 7.3.1 (b), the long-term bonds are higher yielding (or cheaper) than the
short-term bonds. This shows the case of an increasing yield curve.




7.3 Theories of the term structure of interest rates                                 95




Figure 7.3.1 (c): Humped yield curve In Figure 7.3.1 (c), the short-term bonds are
generally cheaper than the long bonds, but the very short rates (with terms less than
one year) are lower than the one-year rates.
   The three most popular explanations for the fact that interest rates vary according
to the term of the investment are:

   • Expectations Theory.

   • Liquidity Preference.

   • Market Segmentation.


7.3.2     Expectations Theory
The relative attraction of short- and longer-term investments will vary according to
expectations of future movements in interest rates. An expectation of a fall in interest
rates will make short-term investments less attractive and longer-term investments
more attractive. In these circumstances yields on short-term investments will rise and
yields on long-term investments will fall. An expectation of a rise in interest rates
will have the converse effect.
   In Figure 7.3.1 (a) it appears that the demand for long-term bonds may be greater
than for short, implying an expectation that interest rates will fall. By buying long-
term bonds investors can continue getting higher rates after a future fall in interest
rates, for the duration of the long bond.
   In Figure 7.3.1 (b) the demand is higher for short-term bonds - perhaps indicating
an expectation of a rise in interest rates.


7.3.3     Liquidity Preference
Longer dated bonds are more sensitive to interest rate movements than short dated
bonds. It is assumed that riskaverse investors will require compensation (in the form
of higher yields) for the greater risk of loss on longer bonds. This might explain some
7.3 Theories of the term structure of interest rates                                 96


of the excess return offered on long-term bonds over short-term bonds in Figure 7.3.1
(b).


7.3.4     Market Segmentation
Bonds of different terms are attractive to different investors, who will choose assets
that are similar in term to their liabilities. The liabilities of banks, for example,
are very short-term (investors may withdraw a large proportion of the funds at very
short notice); hence banks invest in very short-term bonds. Many pension funds have
liabilities that are very long-term, so pension funds are more interested in the longest
dated bonds. The demand for bonds will therefore differ for different terms. The
supply of bonds will also vary by term, as governments and companies’ strategies may
not correspond to the investors’ requirements. The market segmentation hypothesis
argues that the term structure emerges from these different forces of supply and
demand.


7.3.5     Yields to maturity
The yield to maturity for a coupon paying bond (also called the redemption yield)
has been defined as the effective rate of interest at which the discounted value of the
proceeds of a bond equal the price. It is widely used, but has the disadvantage that it
depends on the coupon rate of the bond, and therefore does not give a simple model
of the relationship between term and yield.
   In the UK, yield curves plotting the average (smoothed) yield to maturity of
coupon paying bonds are produced separately for ‘low coupon’, ‘medium coupon’ and
‘high coupon’ bonds.


7.3.6     Par yields
The n-year par yield represents the coupon per £1 nominal that would be payable
on a bond with term n years, which would give the bond a current price under the
current term structure of £1 per £1 nominal, assuming the bond is redeemed at par.
   That is, if ycn is the n-year par yield,

                     1 = (ycn ) vy1 + vy22 + vy33 + . . . + vynn + 1vynn
                                                                


   The par yields give an alternative measure of the relationship between the yield
and term of investments. The difference between the par yield rate and the spot rate
is called the coupon bias.


7.4 Duration, convexity and immunisation                                                97


7.4      Duration, convexity and immunisation
In this part, we consider simple measures of vulnerability to interest rate movements.
For simplicity we assume a flat yield curve, and that when interest rates change, all
change by the same amount, so that the curve stays flat. A flat yield curve implies
that yt = ft,r = i for all t, r and Yt = Ft,r = Ft = δ for all t, i.


7.4.1     Interest rate risk
Suppose an institution holds assets of value VA , to meet liabilities of value VL . Since
both VA and VL represent the discounted value of future cashflows, both are sensitive
to the rate of interest. We assume that the institution is healthy at time 0 so that
currently VA ≥ VL .
   If rates of interest fall, both VA and VL will increase. If rates of interest rise
then both will decrease. We are concerned with the risk that following a downward
movement in interest rates the value of assets increases by less than the value of
liabilities, or that, following an upward movement in interest rates the value of assets
decreases by more than the value of the liabilities.
   In order to examine the impact of interest rate movements on different cashflow
sequences we will use changes in the yield to maturity to represent changes in the un-
derlying term structure. This is approximately (but not exactly) the same as assuming
a constant movement of similar magnitude in the one-period forward rates.


7.4.2     Effective duration
One measure of the sensitivity of a series of cashflows to movements in the interest
rates, is the effective duration (or volatility). Consider a series of cashflows {Ctk } for
k = 1, 2, . . . , n. Let A be the present value of the payments at rate (yield to maturity)
i, so that:
                                            n
                                            X
                                       A=         Ctk vitk                           (7.1)
                                            k=1

   Then the effective duration is defined to be:

                                 1 d          A′
                        v(i) = −      A=−
                                 A di         A                     !
                                               Xn
                             = Pn           tk       Ctk tk vitk +1
                                   k=1 Ctk vi    k=1

   This is a measure of the rate of change of value of A with i, which is independent
of the size of the present value. Equation (2.92) assumes that the cashflows do not
7.4 Duration, convexity and immunisation                                               98


depend on the rate of interest.
     For a small movement ε in interest rates, from i to i+ε, the relative change in value
of the present value is approximately −εv(i) so the new present value is approximately
A(1 − εv(i)).


7.4.3        Duration
Another measure of interest rate sensitivity is the duration, also called Macauley
Duration or discounted mean term. This is the mean term of the cashflows {Ctk },
weighted by present value. That is, at rate i, the duration of the cashflow sequence
{Ctk } is:
                                      Pn
                                            tk Ctk vitk
                                   τ = Pk=1
                                         n         tk
                                         k=1 Ctk vi

     Comparing this expression with the equation for the effective duration it is clear
that:


                                      τ = (1 + i)v(i)

     Another way of deriving the Macauley duration is in terms of the force of interest,
δ:

                                      1 d       di
                               τ =−        A = v(i)
                                      A dδ      dδ
                                             di
                               i = eδ − 1 ⇒      = eδ
                                             dδ
                                ⇒ τ = eδ v(i) = (1 + i)v(i)
     The equation for τ in terms of the cashflows Ctk may be found by differentiating
A with respect to δ, recalling that vitk = e−δtk
     The duration of an n-year coupon paying bond, with coupons of D payable annu-
ally, redeemed at M , is:

                                     D(Ia) n + M nv n
                                  τ=
                                      Da n + M v n
     The duration of an n-year zero coupon bond of nominal amount 100 , say, is:

                                          100nv n
                                     τ=           =n
                                           100v n
     Note that another definition of duration exists: the modified duration. This
can be expressed in terms of the Macauley Duration as


7.4 Duration, convexity and immunisation                                                    99



                                              τ
                                                  (p)
                                           1 + ip

   where i(p) and p are as defined earlier.


7.4.4     Convexity
The convexity of the cashflow series {Ctk } is defined as:

                         1 d2       A′′
                    c(i) =     A =
                         A di2       A                                 !
                                         Xn
                        = Pn          tk       Ctk tk (tk + 1) vitk +2
                             k=1 Ctk vi    t=1

   Combining convexity and duration gives a more accurate approximation to the
change in A following a small change in interest rates. For small ε :

             A(i + ε) − A(i)   ∂A  1              ∂ 2A 1
                             =    × × ε + 1/2 × 2 × × ε2 + · · ·
                    A          ∂i  A              ∂i   A
                             ≈ −εv(i) + 1/2ε c(i)
   Convexity gives a measure of the change in duration of a bond when the interest
rate changes. Positive convexity implies that τ (i) is a decreasing function of i. This
means, for example, that A increases more when there is a decrease in interest rates
than it falls when there is an increase of the same magnitude in interest rates.


7.4.5     Immunisation
Consider a fund with asset cashflows {Atk } and liability cashflows {Ltt }. Let VA (i)
be the present value of the assets at effective rate of interest i and let VL (i) be the
present value of the liabilities at rate i; let vA (i) and vL (i) be the volatility of the
asset and liability cashflows respectively, and let cA (i) and cL (i) be the convexity of
the asset and liability cashflows respectively.
   At rate of interest i0 the fund is immunised against small movements in the rate
of interest of ε if and only if VA (i0 ) = VL (i0 ) and VA (i0 + ε) ≥ VL (i0 + ε).
   Then consider the surplus S(i) = VA (i) − VL (i). From Taylor’s theorem:

                                                          ε2 ′
                      s (i0 + ε) = S (i0 ) + εS (i0 ) +     S (i0 ) + · · ·
   Consider the terms on the right-hand side. We know that S (i0 ) = 0.
   The second term, εS ′ (i0 ), will be equal to zero for any values of ε (positive or
negative) if and only if S ′ (i0 ) = 0, that is if VA′ (i0 ) = VL′ (i0 ). This is equivalent to

7.4 Duration, convexity and immunisation                                                100


requiring that vA (i) = vL (i) or (equivalently) that the durations of the two cashflow
series are the same.
   In the third term, ε2 is always positive, regardless of the sign of ε. Thus, if we
ensure that S ′ (i0 ) > 0, then the third term will also always be positive.
   This is equivalent to requiring that VA′′ (i0 ) > VL′′ (i0 ), which is equivalent to re-
quiring that cA (i) > cL (i).
   For small |ε | the fourth and subsequent terms in the Taylor expansion will be
very small. Hence, given the three conditions above, the fund is protected against
small movements in interest rates. This result is known as Redington’s immunisation
after the British actuary who developed the theory.
   The conditions for Redington’s immunisation may be summarised as follows:

   1. VA (i0 ) = VL (i0 ) - that is, the value of the assets at the starting rate of interest
      is equal to the value of the liabilities.

   2. The volatilities of the asset and liability cashflow series are equal, that is,


                                        vA (i0 ) = vL (i0 ) .

   3. The convexity of the asset cashflow series is greater than the convexity of the
      liability cashflow series - that is,

                                        cA (i0 ) > cL (i0 ) .


   In practice there are difficulties with implementing an immunisation strategy based
on these principles. For example, the method requires continuous rebalancing of port-
folios to keep the asset and liability volatilities equal. There may be options or other
uncertainties in the assets or in the liabilities, making the assessment of the cashflows
approximate rather than known. Assets may not exist to provide the necessary overall
asset volatility to match the liability volatility. Despite these problems, immunisation
theory remains an important consideration in the selection of assets.



