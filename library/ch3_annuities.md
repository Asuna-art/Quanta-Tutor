# 第3章 年金与现值方程

Chapter 3

Compound Interest Functions

3.1      Overview
In this chapter we consider the particular case that the force of interest and therefore
other interest rate quantities are independent of time. We define standard actuarial
notation for the present values of simple payment streams called annuities, which can
be used to construct more complicated payment streams in practical applications.
Closed-form expressions to evaluate the present values and accumulations of various
types of annuity are derived. The concept of an equation of value is discussed, which
is of fundamental importance to the analysis of cash flows in various applications
throughout the remainder of this module.

   • The equation of value is a mathematical expression that equates the present
      value (at a particular time) of the constituent cash flows of a transaction to zero.
      Discounting is expressed in terms of δ. The equivalent expression expressed in
      terms of i is called the yield equation.

   • Standard notation exists for the present value of regular streams of cash flows
      called annuities. These can be used to construct the equations of value for more
      complicated cash flows.

   • Annuities can be immediate or deferred, paid in arrears, in advance or contin-
      uously, and be level or increasing. Closed-form expressions can be derived to
      evaluate the present values of all such annuities.

   • The accumulated value at time n of an n-year annuity can be obtained by
      accumulating the present value at t = 0 through n years. Standard notation
      exists for all such accumulations.

   • i(p) is the nominal rate of interest converted pthly. It is defined such that the

3.2 Interest rate quantities                                                            43


      effective rate of interest over a period of length 1/p is i(p) /p. Therefore,
                                                                p
                                                         i(p)
                                                  
                                      (1 + i) =       1+
                                                          p

   • d(p) is the nominal rate of discount converted pthly. It is defined such that the
      effective rate of discount over a period of length 1/p is d(p) /p. Therefore,
                                                                p
                                                         d(p)
                                                  
                                      (1 − d) =       1−
                                                          p

   • When n is an integer multiple of p, well-defined and standard notation exists
      for the present and accumulated values of n-year annuities paid p thly, with the
      usual variations of in arrears, in advance, and deferred payment.


3.2      Interest rate quantities
The particular case in which δ(t), the force of interest per unit time at time t, does
not depend on t is of special importance. In this situation we assume that, for all
values of t,
                                          δ(t) = δ                                    (3.1)

where δ is some constant. Throughout this chapter, we shall assume that Eq (3.1) is
valid, unless otherwise stated.
   The value at time s of 1 due at time s + t is
                           Z s+t             Z s+t     
                       exp −      δ(r)dr = exp −      δdr
                                  s                             s

                                              = exp(−δt)

which does not depend on s, only the time interval t. Therefore, the value at any
given time of a unit amount due after a further period t is

                                      v(t) = e−δt                                     (3.2)
                                           = vt                                       (3.3)
                                           = (1 − d)t                                 (3.4)

where v and d are defined in terms of δ by the equations

                                          v = e−ô                                    (3.5)


3.2 Interest rate quantities                                                          44


and
                                       1 − d = e−δ                                  (3.6)

Then, in return for a repayment of a unit amount at time 1 , an investor will lend an
amount (1 − d) at time 0 . The sum of (1 − d) may be considered as a loan of 1 (to
be repaid after 1 unit of time) on which interest of amount d is payable in advance.
For this reason, d is called the rate of discount per unit time. Sometimes, in order to
avoid confusion with nominal rates of discount (see Chapter 4), d is called the effective
rate of discount per unit time.
   Similarly, it follows immediately from Eq (2.26) that the accumulated amount at
time s + t of 1 invested at time s does not depend on s and is given by

                                     F (t) = eδt                                    (3.7)
                                          = (1 + i)t                                (3.8)

where i is defined by the equation

                                       1 + i = eδ                                   (3.9)

Therefore, an investor will lend a unit amount at time t = 0 in return for a repayment
of (1 + i) at time t = 1. Accordingly, i is called the rate of interest (or the effective
rate of interest) per unit time.
   Although we have chosen to define i, v, and d in terms of the force of interest δ,
any three of i, v, d, and δ are uniquely determined by the fourth. For example, if we
choose to regard i as the basic parameter, then it follows from Eq (3.9) that

                                      δ = ln(1 + i)

In addition, Eqs (3.5) and (3.9) imply that

                                     v = (1 + i)−1

while Eqs (3.6) and (3.9) imply that

                                   d = 1 − (1 + i)−1
                                         i
                                     =
                                       1+i

These last three equations define δ, v, and d in terms of i.




3.2 Interest rate quantities                                                                   45


   The last equation may be written as

                                             d = iv

which confirms that an interest payment of i at time t = 1 has the same value as a
payment of d at time t = 0. But what sum paid continuously (at a constant rate)
over the time interval [0, 1] has the same value as either of these payments? Let the
required amount be σ such that the amount paid in time increment dt is σdt. Then,
taking values at time 0 , we have
                          Z 1
                     d=    σe−δt dt
                           1 − e−δ
                                  
                      =σ                     ( if δ ̸= 0)     (by Eq (3.6)
                              δ
                          
                           d
                      =σ
                           δ

Hence σ = δ. This result is also true, of course, when δ = 0. This establishes the
important fact that a payment of δ made continuously over the period [0, 1] has the
same value as a payment of d at time 0 or a payment of i at time 1. Each of the three
payments may be regarded as alternative methods of paying interest on a unit loan
over the period.
   In certain situations, it may be natural to regard the force of interest as the basic
parameter, with implied values for i, v, and d. In other cases, it may be preferable
to assume a certain value for i (or d or v ) and to calculate, if necessary, the values
implied for the other three parameters.


          Value Of         δ             i                     v              d
          In Terms Of
          δ                              eδ − 1                e−δ            1 − e−δ
          i                ln(1 + i)                           (1 + i)−1      i(1 + i)−1
          v                − ln v        v −1 − 1                             1−v
                                                    −1
          d                − ln(1 − d)   (1 − d)         −1    1−d


   When i is small, approximate formulae for d and δ in terms of i may be obtained
from well-known series by neglecting the remainder after a small number of terms.
For example, since

                     δ = ln(1 + i)
                             1     1  1
                       = i − i2 + i3 − i4 + · · ·              (if |i| < 1)
3.3 The equation of value                                                                            46


it follows that, for small values of i,

                                              δ ≈ i − i2

Similarly
                           d = i(1 + i)−1
                             = i 1 − i + i2 − i3 + · · ·
                                                               
                                                                    ( if |i| < 1)
                             = i − i2 + i3 − i4 + · · ·
so, if i is small,
                                               d ≈ i − i2

We note that if i is small, then i, δ, and d are all of the same order of magnitude.
Similar expressions can be derived, which give approximate relations between any of
combination of d, δ, and i.


3.3       The equation of value
Consider a transaction under which, in return for outlays of amount at1 , at2 , . . . , atn at
times t1 , t2 , . . . , tn , an investor will receive payments of bt1 , bt2 , . . . , btn at these times,
respectively. (In most situations, only one of atr and btr will be non-zero.) At what
force or rate of interest does the series of outlays have the same present value as the
series of receipts?
    At force of interest δ, the two series are of equal present value if and only if
                                     n
                                     X                   n
                                                         X
                                           atr e−δtr =         btr e−δtr                         (3.10)
                                     r=1                 r=1


This equation may be written as
                                            n
                                            X
                                                  ctr e−δtr = 0                                  (3.11)
                                            r=1


where
                                             ctr = btr − atr

is the amount of the net cash flow at time tr . Note that we adopted the standard
convention that a negative cash flow corresponds to a payment by the investor and
a positive cash flow represents a payment to him. Equation (3.11) expresses alge-
braically the condition that, at force of interest δ, the total value of the net cash
flows is 0 ; it is called the equation of value for the force of interest implied by the

3.3 The equation of value                                                                  47


transaction. If we let eδ = 1 + i, the equation may be written as
                                       n
                                       X
                                                 ctr (1 + i)−tr = 0                     (3.12)
                                        r=1


The latter form is known as the equation of value for the rate of interest or the yield
equation. Alternatively, the equation may be written as
                                                 n
                                                 X
                                                       ctr v tr = 0
                                                 r=1


Note that in the preceding equations n may be infinite.
   In relation to continuous payment streams, if we let ρ1 (t) and ρ2 (t) be the rates
of paying and receiving money at time t, respectively, we call ρ(t) = ρ2 (t) − ρ1 (t) the
net rate of cash flow at time t. The equation of value, corresponding to Eq (3.11), for
the force of interest is                Z ∞
                                                   ρ(t)e−δt dt = 0                      (3.13)

When both discrete and continuous cash flows are present, the equation of value is
                              n
                              X                        Z ∞
                                            −δtr
                                    ctr e          +         ρ(t)e−δt dt = 0            (3.14)
                              r=1                       0


and the equivalent yield equation is
                       n
                       X                               Z ∞
                                            −tr
                             ctr (1 + i)           +         ρ(t)(1 + i)−t dt = 0       (3.15)
                       r=1                              0


For any given transaction, Eq (3.14) may have no roots, a unique root, or several roots
in δ. We consider only real roots as δ has a physical meaning. If there is a unique
root, δ0 say, it is known as the force of interest implied by the transaction, and the
corresponding rate of interest i0 = eδ0 − 1 is called the yield per unit time. Alternative
term for the yield is the internal rate of return for the transaction.
   The analysis of the equation of value for a given transaction may be somewhat
complex. However, when the equation f (i) = 0 is such that f is a monotonic function,
its analysis is particularly simple. The equation has a root if and only if we can find
i1 and i2 with f (i1 ) and f (i2 ) of opposite sign. In this case, the root is unique and
lies between i1 and i2 . By choosing i1 and i2 sufficiently close to each other, we may
determine the yield to any desired degree of accuracy.
   It should be noted that, after multiplication by (1 + i)t0 , Eq (3.12) takes the



3.4 Annuities-certain: present values and accumulations                              48


equivalent form
                                 n
                                 X
                                       ctr (1 + i)t0 −tr = 0                     (3.16)
                                 r=1

This slightly more general form may be called the equation of value at time t0 . It is,
of course, directly equivalent to the original equation (which is now seen to be the
equation of value at time 0), as expected from Eq (3.16).


3.4      Annuities-certain: present values and accumu-
         lations
Consider a series of n payments, each of amount 1 , to be made at time intervals of
one unit, the first payment being made at time t + 1. Such a sequence of payments is
illustrated in Figure 3.4.1, in which the r th payment is made at time t + r.
5-year annuity in arrears:




5-year annuity in advance:




FIGURE 3.4.1: Cash flow diagram for unit annuities paid in arrears and advance

   The present value of this series of payments one unit of time before the first
payment is made is denoted by an . For the series of payments illustrated in Figure
3.4.1, the value relates to time t. Clearly, if i = 0, then an = n; otherwise,

                              an = v + v 2 + v 3 + . . . + v n
                                   v (1 − v n )
                                 =
                                      1−v
                                    1 − vn                                       (3.17)
                                 = −1
                                   v −1
                                   1 − vn
                                 =
                                      i

If n = 0, an is defined to be zero, as no payments will be made.
   In general, the quantity an is the present value at the start of any period of length
n of a series of n payments, each of unit amount, to be made in arrears at unit
time intervals over the period. It is common to refer to such a series of payments,
3.4 Annuities-certain: present values and accumulations                               49


made in arrears, as an immediate annuity-certain and to call an the present value of
the immediate annuity-certain. When there is no possibility of confusion with a life
annuity, i.e., a series of payments dependent on the survival of one or more human
lives, the term annuity may be used as an alternative to annuity-certain, and an
simply may be termed the present value of an n-year annuity paid in arrears.
   The value of this series of payments at the time the first payment is made is
denoted by än . If i = 0, then än = n; otherwise,

                             än = 1 + v + v 2 + . . . + v n−1
                                   1 − vn
                                 =                                                (3.18)
                                    1−v
                                   1 − vn
                                 =
                                      d

In general, the quantity än is the value at the start of any given period of length n
of a series of n payments, each of unit amount, to be made in advance at unit time
intervals over the period. It is common to refer to such a series of payments, made
in advance, as an annuity-due and to call än the present value of the annuity-due or
simply the present value of an n-year paid in advance. Again, if n = 0, än is defined
to be zero.
   It follows directly from the preceding definitions that, for n ≥ 2,
                                                       )
                                     än = (1 + i)an
                                                                                  (3.19)
                                     än = 1 + an−1

These relationships can be verified algebraically and by general reasoning.
   The accumulated value of the series of payments at the time the last payment is
made is denoted by sn . The value one unit of time after the last payment is made is
denoted by s̈n . If i = 0, then sn = s̈n = n, otherwise,

                  sn = (1 + i)n−1 + (1 + i)n−2 + (1 + i)n−3 + · · · + 1
                     = (1 + i)n an                                                (3.20)
                                 n
                         (1 + i) − 1
                     =
                               i

and
                s̈n = (1 + i)n + (1 + i)n−1 + (1 + i)n−2 + · · · + (1 + i)
                   = (1 + i)n än                                                 (3.21)
                             n
                       (1 + i) − 1
                   =
                            d
It is clear that sn and s̈n are the values at the end of any period of length n (i.e., at
time t = n ) of a series of n payments, each of amount 1 , made at unit time intervals
3.4 Annuities-certain: present values and accumulations                                           50


over the period, where the payments are made in arrears and in advance, respectively.
Sometimes sn and s̈n are called the accumulation (or the accumulated amount) of
an immediate annuity and an annuity-due, respectively. When n = 0, sn and sn are
defined to be zero.
   It is an immediate consequence of the preceding definition that
                                                          
                                    s̈n       = (1 + i)sn 
                                                          
                                  sn+1        = 1 + s̈n                                        (3.22)
                                                               
                                    s̈n       = sn+1 − 1
                                                               


   Equations (3.17), (3.18), (3.20), and (3.21) may be expressed in the form
                                                        
                                          1 = ian + v n 
                                                        
                                                        
                                                      n 
                                                        
                                          1 = dä + v
                                                    n
                                          n
                                                                                               (3.23)
                                (1 + i)        = isn + 1  
                                                          
                                                          
                                (1 + i)n
                                                          
                                               = ds̈n + 1 

respectively. The first equation is simply the equation of value at time 0 for a unit
loan over the period from time 0 to time n, when interest is payable in arrears. The
other three equations may be similarly interpreted, the last two being equations of
value at time n.
                                                                   Pn       r
   As the rate of interest i increases, v decreases, so             r=1 v       decreases. Therefore,
for a fixed value of n, an is a decreasing function of i. Similarly, än is a decreasing
function of i, while sn and s̈n are increasing functions of i.
   For a fixed rate of interest, an , än , sn , and s̈n are all increasing functions of n.
When n becomes infinite, the corresponding annuity (or annuity-due) is known as a
perpetuity (or perpetuity-due). The notations a∞ and ä∞ are used to denote the
corresponding present values; if i > 0,

                                   a∞ = lim an =                                               (3.24)
                                              n→∞          i

and
                                   ä∞ = lim än =                                             (3.25)
                                              n→∞          d
These expressions follow directly from Eqs (3.17) and (3.18).
   It is convenient to have standard tables of annuity and accumulation values at
various rates of interest. In view of the relationship 3.3.3, it is not necessary to give
the values of both an and än ; similarly, the relationship 3.3.6 removes the need to
tabulate both sn and s̈n .
   Considering the quantity an as the value of an n-year payment stream (made in
arrears) at time t, and sn as the value of the same stream at time t + n, it is clear
3.5 Deferred annuities                                                                  51


that
                                     sn = (1 + i)n an                                (3.26)

Similarly,
                                     s̈n = (1 + i)n än                              (3.27)


3.5      Deferred annuities
Suppose that m and n are non-negative integers. The value at time t = 0 of a series of
n payments, each of amount 1 , due at times (m + 1), (m + 2), . . ., (m + n) is denoted
by m| an . This is illustrated in Figure 3.5.1.

3-year annuity in arrears deferred for 2 years:




3-year annuity-due deferred for 2 years:



FIGURE 3.5.1: Cash flow diagrams for deferred annuities

   Such a series of payments may be considered as an immediate annuity, deferred
for m time units. When n > 0, this is denoted by

                     m+1
         m| an = v   + v m+2 + v m+3 + · · · + v m+n
               = v + v 2 + v 3 + · · · + v m+n − v + v 2 + v 3 + · · · + v m
                                                                            
                                                                                     (3.28)
               = vm v + v2 + v3 + · · · + vn
                                              


The last two equations show that

                                    m| an = am+n − am                                (3.29)
                                          = v m an                                   (3.30)

   Either of these two equations may be used to determine the value of a deferred
immediate annuity. Together, they imply that

                                   am+n = am + v m an                                (3.31)

which is often a useful representation.


3.6 Continuously payable annuities                                                    52


   We may define the corresponding deferred annuity-due as

                                                           m
                                              m| än = v       än                 (3.32)


3.6      Continuously payable annuities
Let n be a non-negative number. The value at time 0 of an annuity payable continu-
ously between time 0 and time n, where the rate of payment per unit time is constant
and equal to 1 , is denoted by ān .
   It is straightforward to demonstrate that
                                          Z n
                               ān =              e−δt dt
                                        1 − e−δn                                   (3.33)
                                      =
                                            δ
                                        1 − vn
                                      =          ( if                δ ̸= 0)
                                           δ

During an increment of length dt at time t, the payment element made is dt since
ρ(t) = 1. The present value of this element at time 0 is then e−δt dt, and the entire
present value of the stream is obtained from the integral of this between t = 0 and
t = n. Note that ān is defined even for non-integral values of n. If δ = 0 (or,
equivalently, i = 0 ), ān is, of course, equal to n.
   If m is a non-negative number, we use the symbol m| ān to denote the present value
of a continuously payable annuity of 1 per unit time for n time units, deferred for m
time units                            Z m+n
                           m| ān =                e−δt dt
                                          m
                                                  Z n
                                       −δm
                                 =e         e−δs ds
                                   Z m+n 0          Z m
                                           −δt
                                 =       e     dt −     e−δt dt
                                          0                          0

Hence,

                                      m| ān = ām+n − ām                         (3.34)
                                                  = v m ān                        (3.35)

Since Eq (3.33) may be written as

                                                         1 − vn
                                                                    
                                             i
                                       ān =
                                             δ              i


3.7 Varying annuities                                                                53


it follows immediately that, if n is an integer,

                                      i
                                 ān = an        ( if δ ̸= 0)                    (3.36)
                                      δ

The factor i/δ can be thought of as substituting the denominator of an , i.e., replacing
i with δ.


3.7         Varying annuities
Until now we have considered annuities for which the amount of each payment is
constant. For an annuity in which the payments are not all of an equal amount, it is
a simple matter to find the present (or accumulated) value from first principles. For
example, the present value of such an annuity may always be evaluated as
                                        n
                                        X
                                               Xi v ti
                                         i=1


where the i th payment, of amount Xi , is made at time ti .
   In the particular case when Xi = ti = i, the annuity is known as an increasing
annuity, and its present value is denoted by (Ia)n with

                          (Ia)n = v + 2v 2 + 3v 3 + · · · + nv n                 (3.37)

Hence,
                      (1 + i)(Ia)n = 1 + 2v + 3v 2 + · · · + nv n−1

By subtraction, we obtain

                        i(Ia)n = 1 + v + v 2 + · · · + v n−1 − nv n
                               = än − nv n

and so
                                               än − nv n
                                   (Ia)n =                                       (3.38)
                                                    i
The last equation need not be memorized, as it may be rapidly derived from first
principles. A simple way of recalling Eq (3.38) is to express it in the form

                                   än = i(Ia)n + nv n                           (3.39)

This equation is simply the equation of value for a transaction in which an investor
lends 1 at the start of each year for n years in return for interest at the end of each
year of amount i times the outstanding loan and a repayment of the total amount lent
3.7 Varying annuities                                                                 54


(i.e., n ) after n years. The two sides of the equation represent the value (at the start
of the transaction) of the payments made by the lender and the borrower, respectively.
Numerical values of the function (Ia)n are included in standard compound interest
tables for various i and n.
   The present value of any annuity payable in arrears for n time units for which the
amounts of successive payments form an arithmetic progression can be expressed in
terms of an and (Ia)n . If the first payment of such an annuity is P and the second
payment is (P + Q), the tth payment is (P − Q) + Qt, and the present value of the
annuity is therefore
                                 (P − Q)an + Q(Ia)n

Alternatively, the present value of the annuity can be derived from first principles.
   The notation (Iä)n is used to denote the present value of an increasing annuitydue
payable for n time units, the tth payment (of amount t) being made at time t − 1.

                          (Iä)n = 1 + 2v + 3v 2 + · · · + nv n−1
                                = (1 + i)(Ia)n                                    (3.40)
                                = 1 + an−1 + (Ia)n−1                              (3.41)

For increasing annuities that are payable continuously, it is important to distinguish
between annuities which have a constant rate of payment r (per unit time) throughout
the rth period and annuities which have a rate of payment t at time t. For the former,
the rate of payment is a step function, taking the discrete values 1, 2, . . .. For the
latter, the rate of payment itself increases continuously. If the annuities are payable
                                                                   ¯ n , respectively.
for n time units, their present values are denoted by (Iā)n and (Iā)
   Clearly
                                         n Z r
                                         X                     
                                                           t
                              (Iā)n =                    rv dt
                                         r=1        r−1

and                                            Z n
                                    ¯ n =
                                   (Iā)             tv t dt

Using integration by parts in the second case, it can be verified that

                                            än − nv n
                                   (Iā)n =                                       (3.42)
                                                δ

and
                                    ¯ n =      ān − nv n
                                   (Iā)                                          (3.43)
                                                   δ
Each of the last two equations, expressed in a form analogous to Eq (3.39), may be
easily written down as the equation of value for an appropriate transaction.

3.8 Interest payable pthly                                                                55


                                                                                   ¯ n
   Corresponding to the present values at time t = 0, (Ia)n , (Iä)n , (Iā)n and (Iā)
are the accumulations at time t = n of the relevant series of payments. These ac-
cumulations are denoted by (Is)n , (I s̈)n , (I s̄)n , and (I¯s̄)n , respectively. It follows
that                                                    
                                 (Is)n = (1 + i)n (Ia)n 
                                                        
                                                        
                                                 n
                                                        
                                 (I s̈) = (1 + i) (Iä) 
                                      n                    n
                                                   n
                                                                                      (3.44)
                                 (I s̄)n = (1 + i) (Iā)n 
                                                          
                                                          
                                  ¯               n ¯
                                                          
                                 (I s̄)n = (1 + i) (Iā)n 
The present values of deferred increasing annuities are defined in the obvious manner.
For example,
                                                   m
                                    m| (Ia)n = v       (Ia)n

It is important to realize that in general there is no one correct or ‘best’ method of
solution for many compound interest problems. Provided that you have a good grasp
of the underlying principles, you will be able to use that method which is most suited
to his own approach.


3.8      Interest payable pthly
Suppose that, the force of interest per unit time is constant and equal to δ. Let i and
d be the corresponding rates of interest and discount, respectively. We’ve showed that
d payable at time 0 , i payable at time 1 , and δ payable continuously at a constant
rate over the time interval [0, 1] all have the same value (on the basis of the force of
interest δ ). Each of these payments may be regarded as the interest for the period
[0, 1] payable on a loan of 1 made at time t = 0.
   Suppose, however, that a borrower, who is lent 1 at time t = 0 for repayment at
time t = 1, wishes to pay the interest on his loan in p equal installments over the
interval. How much interest should he pay? This question motivates what follows.
   We define i(p) to be that total amount of interest, payable in equal installments
at the end of each pth subinterval (i.e., at times 1/p, 2/p, 3/p, . . . , 1), which has the
same value as each of the interest payments just described. Likewise, we define d(p)
to be that total amount of interest, payable in equal installments at the start of each
p th subinterval (i.e., at times 0, 1/p, 2/p, . . . , (p − 1)/p), which has the same value as
each of these other payments.
   We may easily express i(p) in terms of i. Since i(p) is the total interest paid, each
interest payment is of amount i(p) /p and, when we consider the present value of the




3.8 Interest payable pthly                                                               56


payments at the end of the interval, our definition implies the following
                                 p
                                 X i(p)
                                           (1 + i)(p−t)/p = i                        (3.45)
                                 t=1
                                       p

or, if i ̸= 0,
                                 i(p) (1 + i) − 1
                                                  
                                                     =i
                                  p (1 + i)1/p − 1
Hence,
                                 i(p) = p (1 + i)1/p − 1
                                                       
                                                                                     (3.46)

and                                         p
                                       i(p)
                                   
                                    1+         =1+i                                  (3.47)
                                        p
Note that the last two equations are valid even when i = 0.
    Equations (3.46) and (3.47) are most important. Indeed, either equation may be
regarded as providing a definition of i(p) . If such a definition is used, it is a trivial
matter to establish Eq (3.45), which shows that i(p) may be interpreted as the total
interest payable p thly in arrears in equal installments for a loan of 1 over one time
unit.
    Likewise, it is a consequence of our definition of d(p) that, when we consider the
present value payments at the start of the interval, the following is true
                                p
                                X d(p)
                                           (1 − d)(t−1)/p = d                        (3.48)
                                 t=1
                                       p

or, if d ̸= 0,
                                d(p) 1 − (1 − d)
                                                 
                                                    =d
                                 p 1 − (1 − d)1/p
Hence,
                                 d(p) = p 1 − (1 − d)1/p
                                                        
                                                                                     (3.49)

and                                         p
                                       d(p)
                                   
                                    1−         =1−d                                  (3.50)
                                        p
Again, the last two equations are important and are valid even when d = 0. Either
may be used to define d(p) , in which case Eq (3.48) is readily verified and our original
definition is confirmed. Note that i(1) = i and d(1) = d. It is usual to include values
of i(p) and d(p) , at least for p = 2, 4, and 12 , in standard compound interest tables.
It is essential to appreciate that, at force of interest δ per unit time, the five series of
payments illustrated in Figure 3.8.1 all have the same value.
    If we choose to regard i(p) or d(p) as the basic quantity, Eqs (3.47) or (3.50) may
3.8 Interest payable pthly                                                           57




FIGURE 3.8.1: Equivalent payments

be used to define i in terms of i(p) or d in terms of d(p) . It is customary to refer
to i(p) and d(p) as nominal rates of interest and discount convertible p thly. For
example, if we speak of a rate of interest of 12% per annum convertible quarterly, we
                                                                              4
have i(4) = 0.12 (with 1 year as the unit of time). Since (1 + i) = 1 + i(4) /4 , this
means that i = 0.125509. Therefore, the equivalent annual rate of interest is 12.5509%.
When interest rates are expressed in nominal terms, it is customary to refer to the
equivalent rate per unit time as an effective rate. Therefore, if the nominal rate of
interest convertible quarterly is i(4) = 12% per annum, the effective rate per annum
is i = 12.5509%.
   The treatment of problems involving nominal rates of interest (or discount) is
almost always considerably simplified by an appropriate choice of the time unit. For
example, on the basis of a nominal rate of interest of 12% per annum convertible
quarterly, the present value of 1 due after t years is
                                         −4t
                                    i(4)
                                 
                          −t
                   (1 + i)     = 1+            (by Eq (3.47))
                                         −4t
                                     0.12
                                                  since i(4) = 0.12
                                                                   
                               = 1+
                               = 1.03−4t

Therefore, if we adopt a quarter-year as our basic time unit and use 3% as the effective
rate of interest, we correctly value future payments.
   The general rule to be used in conjunction with nominal rates is very simple.
Choose as the basic time unit the period corresponding to the frequency with which
3.9 Annuities payable pthly: present values and accumulations                             58


the nominal rate of interest is convertible and use i(p) /p as the effective rate of interest
per unit time. For example, if we have a nominal rate of interest of 18% per annum
convertible monthly, we should take 1 month as the unit of time and 1 12 %(18%/12)
as the rate of interest per unit time.
   Note that i(p) and d(p) are given directly in terms of the force of interest δ by the
equations                                                   )
                                                    
                                   i(p) = p eδ/p − 1
                                                                                      (3.51)
                                   d(p) = p 1 − e−δ/p
                                                        

Since
                         lim x eδ/x − 1 = lim x 1 − e−δ/x = δ
                                                        
                         x→∞                 x→∞

it follows immediately from the Eq (3.51) that

                                  lim i(p) = lim d(p) = δ                             (3.52)
                                  p→∞        p→∞


This is intuitively obvious from our original definitions, since a continuous payment
stream may be regarded as the limit, as p tends to infinity of a corresponding series
of payments at intervals of time 1/p.
   Using the preceding definitions, we can easily establish that

                                 i > i(2) > i(3) > · · · > δ

and
                                 d < d(2) < d(3) < · · · < δ
                                   
so that the sequences i(p)      and d(p) tend monotonically to the common limit δ
from above and below, respectively.


3.9      Annuities payable pthly: present values and
         accumulations
The nominal rates of interest and discount introduced in the preceding section are of
particular importance in relation to annuities which are payable more frequently than
once per unit time. We shall refer to an annuity which is payable p times per unit
time as payable pthly.
                                                            (p)
   If p and n are positive integers, the notation an is used to denote the present
value at time 0 of a level annuity payable p thly in arrears at the rate of 1 per unit
time over the time interval [0, n]. For this annuity the payments are made at times
1/p, 2/p, 3/p, . . . , n, and the amount of each payment is 1/p.
                                                            (p)
   It is a simple matter to derive an expression for an from first principles. However,
3.9 Annuities payable pthly: present values and accumulations                            59


the following argument, possibly less immediately obvious, is an important illustration
of a kind of reasoning which has widespread application.
   By definition, a series of p payments, each of amount i(p) /p in arrears at pthly
subintervals over any unit time interval, has the same present value as a single payment
of amount i at the end of the interval. By proportion, p payments, each of amount
1/p in arrears at p thly subintervals over any unit time interval, have the same present
value as a single payment of amount i/i(p) at the end of the interval. Consider now
                                                    (p)
that annuity for which the present value is an . The p payments after time r − 1 and
not later than time r therefore have the same value as a single payment of amount
i/i(p) at time r. This is true for r = 1, 2, . . . , n, so the annuity has the same value as
a series of n payments, each of amount i/i(p) , at times 1, 2, . . . , n. This means that

                                          (p)      i
                                       an =            an                            (3.53)
                                                  i(p)

The alternative approach, from first principles, is to write
                                          np
                                  (p)
                                          X  1
                                 an =             v t/p
                                          t=1
                                              p
                                        1 v 1/p (1 − v n )
                                      =
                                        p 1 − v 1/p                                  (3.54)
                                              1 − vn
                                      =
                                        p [(1 + i)1/p − 1]
                                        1 − vn
                                      = (p)
                                          i
                           (p)
   Likewise, we define än to be the present value of a level annuity-due payable p
thly at the rate of 1 per unit time over the time interval [0, n]. (The annuity payments,
each of amount 1/p, are made at times 0, 1/p, 2/p, . . . , n − (1/p).) By definition, a
series of p payments, each of amount d(p) /p, in advance at p thly subintervals over
any unit time interval has the same value as a single payment of amount i at the end
of the interval. Hence, by proportion, p payments, each of amount 1/p in advance at
p thly subintervals, have the same value as a single payment of amount i/d(p) at the
end of the interval. This means (by an identical argument to that above) that

                                          (p)      i
                                      än =            an                            (3.55)
                                                  d(p)

It is usual to include the values of i/i(p) and i/d(p) in published tables. This enables
               (p)       (p)
the values of an and än to be calculated easily.




3.9 Annuities payable pthly: present values and accumulations                      60


   Alternatively, from first principles, we may write
                                                np
                                    (p)
                                                X  1
                                  än =                  v (t−1)/p
                                                     p
                                                 t=1                            (3.56)
                                                1 − vn
                                              =
                                                  d(p)

(on simplification), which confirms Eq (3.55). Note that

                                          (p)                  (p)
                                         an = v 1/p än

By combining Eqs (3.53) and (3.55), we obtain

                                        (p)              (p)
                         ian = i(p) an = d(p) än = dän = δān                 (3.57)

each expression being equal to (1 − v n ).
   Note that since
                                 lim i(p) = lim d(p) = δ
                                p→∞                  p→∞

it follows immediately from Eqs (3.54) and (3.56) that

                                         (p)               (p)
                                lim an = lim än = ān
                               p→∞                   p→∞


These equations should be intuitively clear.
                         (p)      (p)
   Similarly, we define sn and s̈n to be the accumulated amounts of the correspond-
ing pthly immediate annuity and annuity-due, respectively. Therefore,

                         (p)                   (p)
                        sn = (1 + i)n an
                                        i
                           = (1 + i)n (p) an               (by Eq (3.53))       (3.58)
                                      i
                               i
                           = (p) sn
                             i

Also
                         (p)                   (p)
                     s̈n = (1 + i)n än
                                      i
                         = (1 + i)n (p) an (by Eq (3.55))                  (3.59)
                                    d
                             i
                         = (p) sn
                           d
   An annuity payable pthly in arrears, under which the payments continue indefi-
nitely, is called a perpetuity payable pthly. When the rate of payment is constant and
                                                                                   (p)
equal to 1 per unit time, the present value of such a perpetuity is denoted by a∞ .
If the payments are in advance, we have a perpetuity-due, with the corresponding

3.10 Annuities payable at intervals of time r, where r > 1                              61

                             (p)
present value denoted by ä∞ .
     Since the payments differ only in the first payment at time 0 , it is clear that

                                        (p)          1    (p)
                                      ä∞ =            + a∞                        (3.60)
                                                     p

By letting n tend to infinity in Eqs (3.54) and (3.56), we obtain (if i > 0 )

                                              (p)        1
                                         a∞ =                                      (3.61)
                                                       i(p)

and
                                           (p)          1
                                         ä∞ =                                     (3.62)
                                                       d(p)
respectively.
     The present values of an immediate annuity and an annuity-due, payable pthly at
the rate of 1 per unit time for n time units and deferred for m time units, are denoted
by                                                                  )
                                         (p)                  (p)
                                    m| an           = v m an
                                         (p)                  (p)
                                    m| än          = v m än
respectively.


3.10        Annuities payable at intervals of time r, where
            r>1
We showed how, by replacing a series of payments to be received by an equivalent
series of payments of equal value, we could immediately write down an expression for
the value of a pthly annuity. This technique of equivalent payments may be used to
value a series of payments of constant amount payable at intervals of time length r,
where r is some integer greater than 1.
     For example, suppose that k and r are integers greater than 1 and consider a series
of payments, each of amount X, due at times r, 2r, 3r, . . . , kr. What is the value of
this series at time 0 on the basis of an interest rate i per unit time?




     FIGURE 3.10.1 Annuity valuation through equivalent payments

                       (p)
3.11 Definition of an for non-integer values of n                                         62


   The situation is illustrated in Figure 3.10.1, which shows the payments of amount
X due at the appropriate times. Let us ”replace” the payment of X due at time r by
a series of r payments, each of amount Y , due at times 1, 2, . . . , r, where Y is chosen
to make these r equivalent payments of the same total value as the single payment
they replace. This means that
                                             Y sr = X

at rate i, or
                                                    X
                                             Y =                                       (3.63)
                                                    sr
Similarly, each payment of amount X can be replaced by r equivalent payments of
amount Y of the same value. Then the original series of payments of X, due every r
th time interval, has the same value as a series of kr payments of Y = X/sr due at
unit time intervals. Hence, the value of the annuity is

                                              X
                                                a                                      (3.64)
                                              sr kr

at rate i. (This result may also be obtained from first principles simply by summing
the appropriate geometric progression.)


                                       (p)
3.11       Definition of an for non-integer values of n
                                                             (p)
Let p be a positive integer. Until now, the symbol an has been defined only when
                                                                                 (p)
n is a positive integer. For certain non-integral values of n, the symbol an has an
intuitively obvious interpretation. For example, it is not clear what meaning, if any,
                                              (4)
may be given to a23.5 , but the symbol a23.5 ought to represent the present value of an
immediate annuity of 1 per annum payable quarterly in arrears for 23.5 years (i.e., a
                                                                          (2)
total of 94 quarterly payments, each of amount 0.25). However, a23.25 has no obvious
meaning.
   Suppose that n is an integer multiple of 1/p, say n = r/p, where r is an integer.
                        (p)
In this case we define an to be the value at time t = 0 of a series of r payments, each
                                                                                 (p)
of amount 1/p, at times 1/p, 2/p, 3/p, . . . , r/p = n. If i = 0, then clearly an = n. If
i ̸= 0, then
                         (p)     1 1/p
                                    v + v 2/p + v 3/p + · · · + v r/p
                                                                      
                       an =
                                 p
                                 1 1/p 1 − v r/p
                                                 
                               = v
                                 p      1 − v 1/p
                                      1 − v r/p
                                                  
                               =
                                 p (1 + i)1/p − 1


                          (p)
3.11 Definition of an for non-integer values of n                                       63


and so                                     (                             )
                                               1−v n
                                    (p)         i(p)
                                                             if i ̸= 0
                                   an =
                                                  n          if i = 0
Note that, by working in terms of a new time unit equal to 1/p times the original
time unit and with the equivalent effective interest rate of i(p) /p per new time unit,
we see that
                                 (p)          1
                                an at rate i = anp at rate i(p) /p
                                              p
                    (p)
The definition of an given above is mathematically meaningful for all non-negative
values of n. For our present purpose, therefore, it is convenient to adopt this definition
for all n.
   Similarly, if i ̸= 0, we define for all non-negative n

                                   (p)                   (p)         n
                                                                             
                                  än = (1 + i)1/p an = 1−v
                                                         d(p)
                                                                             
                                                                             
                                   (p)                 (p)   −1      n
                                  sn = (1 + i)n an = (1+i)
                                                        i(p)
                                   (p)                 (p)     −1    n       
                                  s̈n = (1 + i)n än = (1+i)
                                                                             
                                                          d(p)


where i(p) and d(p) are defined by Eqs 4.1.2 and 4.1.5, respectively. If i = 0, each of
these last three functions is defined to equal n.
   It is a trivial consequence of our definitions that the formulae

                                            (p)         i
                                           an =               an
                                                       i(p)

                                            (p)         i
                                           än =      an
                                                 d(p)
                                             (p)   i
                                           sn = (p) sn
                                                 i
                                             (p)   i
                                           s̈n = (p) sn
                                                 d
(valid when i ̸= 0 ) now hold for all values of n.



