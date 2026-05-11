# 第1章 数据与金融建模

Chapter 1

Data and financial modeling

1.1      Overview
  • Describe the principles of actuarial modelling.

  • Describe why and how models are used including, in general terms, the use of
      models for pricing, reserving, and capital modelling.

  • Explain the benefits and limitations of modelling.

  • Describe, in general terms, how to decide whether a model is suitable for any
      particular application.

  • Explain the difference between the short-run and long-run properties of a model,
      and how this may be relevant in deciding whether a model is suitable for any
      particular application.

  • Describe, in general terms, how to analyse the potential output from a model,
      and explain why this is relevant to the choice of model.

  • Explain the factors that must be considered when communicating the results
      following the application of a model.

  • Describe how to use a generalised cashflow model to describe financial transac-
      tions.

  • State the inflows and outflows in each future time period, and discuss whether
      the amount or the timing (or both) is fixed or uncertain for a given cashflow
      process.

  • Describe in the form of a cashflow model the operation of financial instruments
      (like a zero-coupon bond, a fixed-interest security, an index-linked security, a
1.2 Introduction to Models                                                             8


      current account, cash on deposit, a credit card, an equity, an interest-only loan,
      a repayment loan and an annuity certain) and an insurance contract (like en-
      dowment, term assurance, contingent annuity, car insurance and health cash
      plans).


1.2      Introduction to Models
”A model is like a flashlight in the dark, helping us find our way.” This analogy
encapsulates the essence of models in our quest to understand complex systems and
make informed decisions. Just like a flashlight illuminates unseen obstacles in a dark
room, a model sheds light on the intricate dynamics of real-world scenarios, revealing
patterns, predicting outcomes, and guiding our actions.

Why Do We Use Models? A model is a simplified representation that helps us
grasp complex realities. In various fields, models play a pivotal role:

   • Economics: Economists use models to predict how changes, like increasing
      taxes or lowering interest rates, might affect people’s behavior and the economy
      as a whole. It’s like predicting if changing the price of ice cream might affect
      how many people buy it.

   • Medicine: Doctors and scientists use models to understand diseases and test
      new treatments. For example, they might use a model to predict how fast a
      virus might spread in a town and see how different actions, like social distancing,
      might help.

   • Insurance: In insurance, actuaries use models to predict how likely it is that
      different events will happen, like a person getting sick or a car getting into
      an accident. This helps insurance companies decide how much to charge for
      insurance.


1.2.1     Development of Models
Building a Model: Building a model is similar to assemble a puzzle, where each
piece is a component of the system or process we aim to represent. The complexity
of the puzzle depends on the relationships between different pieces (parameters). For
instance, when modeling a life insurance company, various pieces such as regulations,
taxation, cancellation policies, and future uncertainties like investment returns and
mortality rates need to be meticulously fitted together.


1.2 Introduction to Models                                                            9


   Data Consideration: A model is only as good as the data it is built upon.
Gathering relevant, accurate, and comprehensive data is the cornerstone of model
development. This involves scrutinizing historical data, observing current trends, and
forecasting future changes. The principles and techniques for analyzing such data are
covered in-depth in CS1-Actuarial Statistics, providing a foundation for understanding
variability, uncertainty, and predicting future outcomes.

   Statistical Methods: Once suitable data are identified, statistical methods
come into play to fit this data into the model. This is like measuring and cutting
the puzzle pieces to ensure they fit together perfectly. Techniques such as regression
analysis, hypothesis testing, and maximum likelihood estimation, are used to infer
relationships, validate assumptions, and estimate parameters.

   Objective Consideration: The final shape of the puzzle is determined by the
objectives of modeling. What are we aiming to achieve? Sometimes, it’s not about
creating a picture-perfect representation but about building a pragmatic model that
safeguards against underestimation of costs or risks.


1.2.2    Utilization of Models
A Step-by-Step Approach: The application of models is an intricate, iterative
process, requiring careful consideration at each stage. Here, we delineate each step,
offering insights and details to ensure the development of robust, reliable models.

  1. Define Objectives: Start with clear, well-defined objectives that the modeling
     process needs to meet. This foundational step guides every subsequent decision
     and action in the modeling journey.

  2. Planning and Validation: Develop a detailed plan for the modeling process,
     outlining the methodology, tools, and validation techniques. A well-thought-out
     plan ensures a structured approach and helps anticipate and mitigate challenges.

  3. Data Collection and Analysis: Gather and meticulously analyze the neces-
     sary data, which forms the backbone of your model. Employ statistical tech-
     niques to uncover patterns, relationships, and insights that inform the model’s
     structure and parameters.

  4. Parameter Definition and Value Assignment: Identify and define the
     model’s parameters, considering appropriate values based on data analysis. This
     step shapes the model, determining its behavior and responsiveness to various
     inputs.
1.2 Introduction to Models                                                         10


  5. Model Definition and Refinement: Begin by crafting a model that captures
    the essence of the real-world system, then refine it by adding complexity and
    detail. This iterative process improves the model’s accuracy and representative-
    ness.

  6. Expert Consultation: Seek feedback from experts knowledgeable about the
    system being modeled. Their insights can validate your model, challenge as-
    sumptions, and guide refinements to better align with real-world dynamics.

  7. Tool Selection and Implementation: Decide on the appropriate tools or
    languages for model implementation and ensure the reliability of the chosen
    random number generator, especially in the context of the model’s complexity.

  8. Program Development and Debugging: Write and debug the computer
    program representing the model, ensuring accurate execution of the model’s
    operations and alignment with the defined structure.

  9. Output Evaluation: Assess the reasonableness of the model’s output, com-
    paring results to expectations and making necessary adjustments to enhance
    accuracy and reliability.

 10. Robustness Review: Review the appropriateness of the model by testing
    its sensitivity to small changes in input parameters. This step helps identify
    vulnerabilities and assess the model’s stability and reliability.

 11. Output Analysis: Analyze the results produced by the model, drawing conclu-
    sions, identifying trends, and uncovering insights that inform decision-making
    and strategy.

 12. Compliance with Professional Guidance: Ensure that the model adheres
    to relevant professional standards and guidelines, such as the Technical Actuarial
    Standard (TAS100) issued by the Financial Reporting Council, which governs
    technical actuarial work.

 13. Communication of Results: Clearly and effectively communicate the model’s
    results, assumptions, limitations, and implications to stakeholders, ensuring
    transparency and understanding.

 14. Documentation: Maintain thorough documentation of the model, its develop-
    ment process, parameters, and results. This ensures reproducibility, facilitates
    future refinements and serves as a reference for stakeholders and practitioners.



1.2 Introduction to Models                                                          11


1.2.3    Benefits and Limitations of Modeling
Benefits of modelling.

   • Compressed timeframe: We are able to compress the time it takes to examine
     the results of a real world system. This is particularly useful in actuarial work,
     where financial planning is required, often for events far in the future. For
     example, funding a pension scheme, where contributions to the scheme are made
     now towards pensions that may be paid many years in the future.

   • Ability to incorporate randomness: Standard mathematical or logical mod-
     els are not always capable of allowing for the random elements, such as interest
     rates, life expectancy or currency rates, and for correlations between such ele-
     ments. The nature of such random elements is often important to include in a
     model, enabling the user to see the range of possible outcomes. Such randomness
     can be incorporated into stochastic models.

   • Scenario testing: Models enable us to run several different scenarios, varying
     parameters, and to easily observe the effects of such variation. For example,
     we could see the expected increase in pension resulting from paying a larger
     percentage of salary into a personal pension plan.

   • Greater control over experimental conditions: A model allows us to set up
     the experimental conditions. This is in contrast to a real world system where we
     often do not have the ability to influence some of the conditions. This allows us
     to examine the output from a model, without encountering unnecessary variation
     in the results.

   • Cost control: By building a model to represent a real world system we can
     avoid making costly investments in the actual system before fully understanding
     the implications.



Limitations of modelling. Whilst models are extremely useful when dealing with
actuarial problems, they have their limitations. Modelling a process is not always the
most effective or efficient way to approach the problem. We have explained some of
the general drawbacks/limitations that can occur below.

   • Time and cost: Modelling complex systems can require the investment of a
     significant amount of time and expertise. This, in turn, leads to a significant
     cost to the client.

1.3 Characteristics of Models                                                         12


   • Several runs required: For a stochastic model, each run is only an estimate
      of a model’s output. The model needs to be run a number of times to construct
      an accurate indication of the distribution of the potential outcome. Generally,
      models are more useful to examine the effects of different input parameters than
      to optimise outputs.

   • Validation and verification: It is not easy to see past the complexity of a
      model in order to ensure that it actually mimics the real world system.

   • Reliance on data input: The model relies on accurate data being used to set
      up and parametrise the model. If this is not the case, the model is likely to be
      inappropriate, i.e. rubbish in, rubbish out.

   • Inappropriate use: The model must be properly understood by its user and
      communicated appropriately to the client. Without this level of understanding,
      there is scope for the model to be applied in the wrong situations.

   • Limited scope: It is not possible to create a model which covers all possible
      future events. For example, the introduction of new legislation may invalidate
      the results of our model. However, we are not always able to anticipate such a
      change.

   • Difficulty interpreting some outputs: Some results may only make sense in
      a relative sense e.g. they allow us to understand the effects of varying different
      input parameters has on the output, but the actual output on its own may add
      little or no understanding to the real world system as a single output.


1.3      Characteristics of Models
1.3.1     Stochastic vs. Deterministic Models
When we try to represent reality through models, we often deal with uncertainties and
randomness. Imagine you’re tossing a coin; you can’t be sure whether it will land on
heads or tails. This uncertainty and randomness can be represented using stochastic
models. In contrast, deterministic models don’t have any randomness; they’re like a
recipe, where you get the same cake every time if you follow the instructions exactly.

1. Deterministic Models: Deterministic models are like cooking with a recipe.
If you have a set of ingredients (inputs) and follow the steps (relationships) exactly,
you’ll get the same result every time. These models are often simpler and can be solved
using direct calculation or numerical approximations. However, they only represent a
single scenario, which can be a limitation if we want to explore different possibilities.
1.3 Characteristics of Models                                                          13


2. Stochastic Models: Contrarily, stochastic models acknowledge the randomness
inherent in real-world scenarios. In these models, inputs are represented as random
variables, leading to varied outputs each time the model is run, even with the same
initial conditions.
   Imagine an insurance company trying to predict the number of claims it will receive
in a month. The company can’t know this number for sure, as it depends on random
events like accidents or illnesses. A stochastic model would use historical data to assign
probabilities to different numbers of claims, providing a range of possible outcomes
and their likelihoods.

   Monte Carlo Simulation: Monte Carlo simulation is a technique used to un-
derstand the variability in stochastic models. It involves running the model numerous
times with different random inputs and observing the range of outcomes. This helps
in estimating the probabilities of different results and understanding the risk and
uncertainty associated with the model.
   Continuing with the insurance example, the company could use Monte Carlo sim-
ulation to run the model thousands of times, each time with a different set of random
inputs representing the occurrence of claims. This would yield a distribution of pos-
sible total claims for the month, helping the company assess the risk and set aside an
appropriate reserve of funds.
   When feasible, deriving results using analytical methods is advantageous as it offers
precise results and facilitates the analysis of assumption changes. However, many real-
world problems are intricate, necessitating the versatility of Monte Carlo simulation.
But if even part of a model can be treated analytically, it may provide a check on any
simulation method used. It may be possible to use a deterministic method to calculate
the expected values, or possibly the median values, for a complicated problem, where
the distributions around these central values are estimated by simulation.
   Simulation methods excel in providing ’what if?’ answers, exploring the implica-
tions of various assumptions. However, identifying the optimal set of assumptions to
maximize or minimize a specific result is a complex task. The precision of simulated
results is proportional to the number of simulations conducted, necessitating a balance
between computational cost and accuracy.
   To summarize, models are our key to unlocking the complexities of the real world.
Deterministic models offer simplicity and consistency, providing a clear path in a sce-
nario where randomness is absent. On the other hand, stochastic models embrace the
uncertainties inherent in many real-world situations, offering a spectrum of possible
outcomes and insights into their probabilities.
   Monte Carlo simulation stands as a pivotal technique, enabling us to delve deeper
into the intricacies of stochastic models and assess various scenarios, risks, and uncer-
1.3 Characteristics of Models                                                          14


tainties. While challenges exist, particularly in optimizing assumptions and balancing
precision with computational resources, the insights gained are invaluable.
   For budding actuaries and analysts, understanding the dynamics of these models
is crucial. They serve as a foundation for predicting future events, assessing risks, and
making informed decisions. As you venture further into your studies and professional
life, you’ll find that the ability to harness the power of these models is an essential
skill in navigating the uncertain terrains of actuarial science and beyond.


1.3.2     Time and State Characteristics
In modeling, the state of a model is defined as the set of variables that describe
the system at a particular point in time, taking into account the goals of the study.
Think of it as a snapshot that captures all the relevant details of a system at a specific
moment, allowing for the representation of any future scenarios as states.


Discrete vs. Continuous States.

   • Discrete States: In discrete states, variables exhibit step function changes in
      time. They jump from one state to another, without any in-between values.
      A vivid example of this is the transition from being alive to dead; there is no
      intermediate state between these two. Similarly, when an insurance company
      issues a new policy, the number of policies increases in discrete steps, each
      representing a change in state.

   • Continuous States: Contrarily, in continuous states, variables change smoothly
      and continuously over time. An example of this can be seen in the real-time
      fluctuations in the values of investments. The value of an investment can take
      any real number and is in a state of constant change, reflecting the dynamic
      nature of financial markets.

The choice between using a discrete or continuous state model is influenced by the
objectives of the study, rather than the inherent nature of the system being modeled.
It’s like to deciding whether to use a series of photographs or a video to capture an
event, based on what aspect we are most interested in observing.


Discrete vs. Continuous Time.
   Models can also represent time in either a discrete or a continuous manner, depend-
ing on the requirements of the study. Discrete time is similar to checking a clock at
regular intervals, with outputs from the model being required only at specific points.
1.3 Characteristics of Models                                                         15


In contrast, continuous time is like a running stopwatch, capturing the ongoing flow
of events.
   However, when employing Monte Carlo simulation for a continuous time problem,
challenges arise. The continuous progression of time must be discretized into man-
ageable steps, much like pausing a video at intervals to observe specific frames. The
finer the time intervals, the clearer the observation, but this also necessitates more
processing time. It’s important to note that some results attainable in continuous
time and space models may not be replicable through discrete simulation.


Short-term vs. Long-term Properties.
   When we create models, we’re essentially crafting a bridge between the complex-
ities of the real world and our understanding of it. These models aim to highlight
patterns, predict outcomes, and guide decisions. Yet, the timeframe we’re considering
plays a significant role in determining how we perceive and evaluate these models.
   A classic example that showcases the difference between short-term and long-term
modeling is the phenomenon of exponential growth. Over a short period of time,
exponential growth can appear linear. This means that if we’re only observing a
small slice of time, we might underestimate the future growth rate.
   If we can anticipate certain changes or trends, it’s beneficial to integrate them into
the model. However, predicting the distant future is fraught with uncertainties. Just
as weather forecasts are more accurate a day in advance than a month ahead, our
models too become less reliable the further we project.
   In our quest to simplify and understand, we sometimes omit intricate ’higher order’
relationships from our models. These might seem inconsequential in the immediate
future but can have amplified effects in the long run. Imagine planting a tree next to
a building. In the short term, there’s no issue. But over the years, as the tree grows,
its roots might interfere with the building’s foundation, a consequence not foreseen in
the initial years.


1.3.3        Specialized Models
In modeling, there are some specialized tools we use to help us understand complex
stuff. These include scenario-based and proxy models. Let’s take a closer look at
what these models are and how they work.

Scenario-based Models

Imagine you’re trying to decide what to wear. You think about different weather
scenarios—rainy, sunny, windy—and choose your outfit based on what you think the
1.4 Model Development and Assessment                                                  16


weather will be like. This is similar to how scenario-based models work. They focus on
a specific scenario or situation and look at the input parameters that fit that scenario.
    In simpler terms, these models help us see what might happen in different situa-
tions. This way, we can make better decisions by understanding the possible outcomes
of each scenario. It’s like picking the best day for an outdoor activity based on the
weather forecast!

Proxy Models

Now, let’s talk about proxy models. In insurance, figuring out the value of assets and
liabilities can be really tricky and time-consuming. This is where proxy models come
in handy. They are like shortcuts, helping us get results faster, even though they
might be a bit less accurate.
    For instance, imagine a car insurance company trying to figure out how much
they’ll pay in claims each year. They might use a Monte Carlo simulation to look
at different scenarios and get a range of possible outcomes. But this can take a long
time. So, they might use a proxy model, like a regression function, to make this
process quicker. This way, they can estimate the total amount of claims paid without
having to do a bunch of complicated calculations.


1.4       Model Development and Assessment
1.4.1      Assessing Model Suitability
To ensure the effectiveness of our model, we need to evaluate various aspects to ensure
its reliability:

    • Objectives of the Modelling Exercise: Define the main goals we aim to
      achieve with this model.

    • Model Validity: Ensure that the model is suitable for our specific purposes.

    • Data Validity: Verify the relevance and reliability of the data we’re using.

    • Assumption Validity: Ensure that our starting assumptions are reasonable
      and reflect real-world conditions.

    • Possible Errors: Recognize that no model is perfect. We need to be aware of
      potential inaccuracies or gaps in representing the real-world scenario.

    • Impact of Correlations: Understand how random variables within the model
      influence one another.
1.4 Model Development and Assessment                                                 17


   • Result Correlations: Consider how the different outputs from the model
      relate to each other.

   • Model Relevance: Regularly update our model to keep it current and in line
      with new data or scenarios.

   • Data Credibility: Ensure that the data we input is trustworthy.

   • Output Credibility: Ensure that our model’s results are consistent and be-
      lievable.

   • Accuracy Concerns: Be cautious of over-relying on extremely precise results,
      which might not always equate to accuracy.

   • Communication Ease: The model and its results should be easy to explain
      and interpret.

   • Regulatory Requirements: Stay informed about any standards or regula-
      tions that our model needs to comply with.


1.4.2     Analyzing and Testing the Model
Modeling is a dynamic process, and it’s essential to continually evaluate and refine
the models we create. This iterative process ensures that our models remain robust,
reliable, and reflective of real-world scenarios.

   • Statistical Sampling: This involves analyzing the model’s output to ensure
      its consistency and reliability. Through statistical sampling, we can gauge the
      likelihood of different outcomes and assess the reliability of our model’s predic-
      tions.

   • Sensitivity Testing: It’s crucial to understand how flexible our model is.
      Sensitivity testing involves altering the model’s inputs slightly and observing
      the resulting changes in outputs. This process helps in:

        – Evaluating the model’s robustness against real-world fluctuations.
        – Identifying which inputs have the most significant impact on the model’s
           results.
        – Detecting potential vulnerabilities in the model, especially if minor changes
           in inputs lead to disproportionately large changes in outputs.
        – Highlighting the key inputs and relationships that need careful considera-
           tion during model design and utilization.
1.5 Communication and Application                                                  18


   • Simulation Experiments: Beyond sensitivity testing, it’s also valuable to
      simulate different scenarios to see how our model performs. Designing and
      running these experiments can provide insights into the model’s behavior under
      various conditions. It’s through such simulation experiments that we can:

        – Refine the model’s parameters for better accuracy.
        – Identify areas of the model that need enhancement or modification.
        – Validate the model’s predictions against known outcomes, if available.

Note: Always remember that a model is only as good as the data it’s based on
and the assumptions it operates under. Regular testing and refining ensure that our
models remain relevant and accurate tools for decision-making. As budding financial
mathematicians, cultivating a habit of rigorous model testing will be invaluable in
your professional journey.


1.5      Communication and Application
1.5.1     Communicating the Results
Sharing our findings is just as crucial as the analysis itself:

   • Reporting and Interpretation: Clearly present the results and explain their
      implications.

   • Effective Communication: Tailor the communication style to the audience,
      ensuring the model’s insights are accessible to everyone.


1.5.2     Applying the Model
With a tested and refined model in hand, we’re ready to use it:

   • Real-world Use Cases: Identify practical applications where our model can
      be a valuable tool.

   • Best Practices: By following established guidelines, we can ensure our model
      is used effectively and responsibly.

   Models are valuable tools for understanding and predicting complex scenarios. By
diligently selecting, testing, and refining them, and then effectively communicating
their results, we can make informed decisions. Always approach modeling with a
critical mind, continuously questioning and refining your methods.
1.6 Generalised cashflow model                                                      19


1.6     Generalised cashflow model
1.6.1    Cashflow process
The practical work of the actuary often involves the management of various cashflows.
These are simply sums of money, which are paid or received at different times. The
timing of the cashflows may be known or uncertain. The amount of the individual
cashflows may also be known or unknown in advance. From a theoretical viewpoint
one may also consider a continuously payable cashflow.
   For example, a company operating a privately owned bridge, road or tunnel will
receive toll payments. The company will pay out money for maintenance, debt re-
payment and for other management expenses. From the company’s viewpoint the toll
payments are positive cashflows (i.e. money received) while the maintenance, debt
repayments and other expenses are negative cashflows (i.e. money paid out). Similar
cashflows arise in all businesses. In some businesses, such as insurance companies, in-
vestment income will be received in relation to positive cashflows (premiums) received
before the negative cashflows (claims and expenses).
   Where there is uncertainty about the amount or timing of cashflows, an actuary
can assign probabilities to both the amount and the existence of a cashflow. In this
subject we will assume that the existence of the future cashflows is certain.


1.6.2    Scenarios with certain cashflows
In this section, we provide examples of practical situations with cashflows that are
assumed to be certain. In reality this may not be the case as the counterparty of a
particular cashflow may not be able to pay out. For example, a company may fail
and not be able to pay out interest on issued bonds.

Zero-coupon bond: The term ’zero-coupon bond’ is used to describe a security
that is simply a contract to provide a specified lump sum at some specified future
date. For the investor there is a negative cashflow at the point of investment and a
single known positive cashflow on the specified future date.

Fixed-Interest Security: A body such as an industrial company, a local authority,
or the government of a country may raise money by floating a loan on the stock
exchange. In many instances such a loan takes the form of a fixed-interest security,
which is issued in bonds of a stated nominal amount. The characteristic feature of
such a security in its simplest form is that the holder of a bond will receive a lump
sum of specified amount at some specified future time together with a series of regular
level interest payments until the repayment (or redemption) of the lump sum.
1.6 Generalised cashflow model                                                        20


   The investor has an initial negative cashflow, a single known positive cashflow on
the specified future date, and a series of smaller known positive cashflows on a regular
set of specified future dates.

Index-Linked Security: With a conventional fixed-interest security the interest
payments are all the same amount. If inflationary pressures in the economy are not
kept under control, the purchasing power of a given sum of money diminishes with
the passage of time, significantly so when the rate of inflation is high. For this reason
some investors are attracted by a security for which the actual cash amount of interest
payments and of the final capital repayment are linked to an ’index’ which reflects
the effects of inflation.
   Here, the initial negative cashflow is followed by a series of unknown positive
cashflows and a single larger unknown positive cashflow, all on specified dates.
   However, it is known that the amounts of the future cashflows relate to the inflation
index. Hence these cashflows are said to be known in ’real’ terms.
   Note that in practice the operation of an index-linked security will be such that
the cashflows do not relate to the inflation index at the time of payment, due to delays
in calculating the index. It is also possible that the need of the borrower (or perhaps
the investors) to know the amounts of the payments in advance may lead to the use
of an index from an earlier period.

Cash on Deposit: If cash is placed on deposit, the investor can choose when to
disinvest and will receive interest additions during the period of investment. The
interest additions will be subject to regular change as determined by the investment
provider. These additions may only be known on a day-to-day basis. The amounts
and timing of cashflows will, therefore, be unknown.

Equity Shares: Equity shares (also known as shares or equities in the UK and as
common stock in the USA) are securities that are held by the owners of an organisa-
tion. Equity shareholders own the company that issued the shares. For example, if a
company issues 4,000 shares and an investor buys 1,000 , the investor owns 25% of the
company. In a small company all the equity shares may be held by a few individuals
or institutions. In a large organisation there may be many thousands of shareholders.
   Equity shares do not earn a fixed rate of interest as fixed-interest securities do.
Instead the shareholders are entitled to a share in the company’s profits, in proportion
to the number of shares owned.
   The distribution of profits to shareholders takes the form of regular payments of
dividends. Since they are related to the company profits that are not known in
advance, dividend rates are variable. It is expected that company profits will increase
1.6 Generalised cashflow model                                                         21


over time and also, therefore, expected that dividends per share will increase - though
there are likely to be fluctuations. This means that in order to construct a cashflow
schedule for an equity it is necessary first to make an assumption about the growth of
future dividends. It also means that the entries in the cashflow schedule are uncertain
- they are estimates rather than known quantities.
   In practice, the relationship between dividends and profits is not a simple one.
Companies will, from time to time, need to hold back some profits to provide funds
for new projects or expansion. They may also hold back profits in good years to
subsidise dividends in years with poorer profits. Additionally, companies may be able
to distribute profits in a manner other than dividends, such as by buying back the
shares issued to some investors.
   Since equities do not have a fixed redemption date, but can be held in perpetuity,
we may assume that dividends continue indefinitely (unless the investor sells the shares
or the company buys them back), but it is important to bear in mind the risk that the
company will fail, in which case the dividend income will cease and the shareholders
would only be entitled to any assets which remain after creditors are paid. The future
positive cashflows for the investor are therefore uncertain in amount and may even be
lower, in total, than the initial negative cashflow.

Interest-Only Loan: An ’interest-only’ loan is a loan that is repayable by a series
of interest payments followed by a return of the initial loan amount.
   In the simplest of cases, the cashflows are the reverse of those for a fixed-interest
security. The provider of the loan effectively buys a fixed-interest security from the
borrower.
   In practice, however, the interest rate need not be fixed in advance. The regular
cashflows may therefore be of unknown amounts.
   It may also be possible for the loan to be repaid early. The number of cashflows
and the timing of the final cashflows may therefore be uncertain.

Repayment Loan or Mortgage: A repayment loan is a loan that is repayable by
a series of payments that include partial repayment of the loan capital in addition to
the interest payments.
   In its simplest form, the interest rate will be fixed and the payments will be of
fixed equal amounts, paid at regular known times. The cashflows are similar to those
for an annuity certain.
   As for the ’interest-only’ loan, complications may be added by allowing the interest
rate to vary or the loan to be repaid early. Additionally, it is possible that the regular
repayments could be specified to increase (or decrease) with time. Such changes could
be smooth or discrete.
1.6 Generalised cashflow model                                                        22


   It is important to appreciate that with a repayment loan the breakdown of each
payment into ’interest’ and ’capital’ changes significantly over the period of the loan.
The first repayment will consist almost entirely of interest and will provide only a very
small capital repayment. In contrast, the final repayment will consist almost entirely
of capital and will have a small interest content.

Annuity Certain: An annuity certain provides a series of regular payments in re-
turn for a single premium (i.e. a lump sum) paid at the outset. The precise conditions
under which the annuity payments will be made will be clearly specified. In particular,
the number of years for which the annuity is payable, and the frequency of payment,
will be specified. Also, the payment amounts may be level or might be specified to
vary - for example in line with an inflation index, or at a constant rate.
   The cashflows for the investor will be an initial negative cashflow followed by a
series of smaller regular positive cashflows throughout the specified term of payment.
In the case of level annuity payments, the cashflows are similar to those for a fixed-
interest security. From the perspective of the annuity provider, there is an initial
positive cashflow followed by a known number of regular negative cashflows. The
theory can be extended to deal with annuities where the payment term is uncertain,
that is, for which payments are made only so long as the annuity policyholder survives.

Credit card: Credit cards allow flexible borrowing, generally known as revolving
credit. Credit card holders can spend up to their agreed credit limit and must pay
back a minimum amount each month. Credit card holders are divided between ’trans-
actors’, who repay in full each month, and ’revolvers’, who take advantage of flexible
borrowing and repayments.
   Credit cards charge interest on amounts borrowed and fees for late payments and
other services. Many ’transactors’ pay no charges on their credit cards. Cashflows on
credit cards are uncertain and are hard to model because they depend on customer
behaviour which can change over time. For example, customers who are getting into
financial difficulties may increase their borrowing up to their agreed credit limit and
then default.

Current account: Current accounts are ’bundled’ products which allow both sav-
ings and borrowing (through overdrafts) and enable payments by various methods
including cash withdrawals, debit cards, direct debits, online and mobile payments
and cheques.
   Current accounts typically charge interest on overdrafts and various fees, which
may include regular monthly charges and/or fees for certain transactions. In the UK,
banks typically do not make monthly charges (except for packaged current accounts
1.6 Generalised cashflow model                                                          23


with loyalty benefits) and many current account customers enjoy ’free-if-in-credit’
banking. As for credit cards, cashflows on current accounts are uncertain and, because
they depend on customer behaviour, are hard to model.

Insurance contracts

The cashflows for the examples covered in this section differ from the previous in that
the frequency, severity, and/or timing of the cashflow may be unknown. For example,
a typical cover of a life cover may have a specified date on which a pre-agreed amount
is paid on survival (Section 2.3.1) - but the benefit payment may not be paid if the
individual does not survive. Similarly, a pension pays out a known amount at a
specified time per month, but only if the individual is alive. Typically the severity is
known and pre-specified in life-insurance contracts.
   On the other hand, a non-life (general) insurance cover tends to not have known
severities. For example, the cost of a car accident may range from a few pounds in
the case of a small collision to millions in case of a major accident that caused death.

Endowment: A pure endowment is an insurance policy which provides a lump sum
benefit on survival to the end of a specified term usually’ in return for a series of
regular premiums. The cashflows for the policyholder will be a series of negative
cashflows throughout the specified term or until death, if earlier. A large, positive
cashflow occurs at the end of the term, only if the policyholder has survived. If the
policyholder dies before the end of the term, there is no positive cashflow.
   From the perspective of the insurer, there is a stream of regular positive cashflows
that ceases at a specified point (or earlier, if the policyholder dies) followed by a large
negative cashflow, contingent on policyholder survival.
   An endowment assurance is similar in that it provides a survival benefit at the
end of the term, but it also provides a lump sum benefit on death before the end of
the term. The benefits are provided in return for a series of regular premiums.
   The cashflows for the policyholder will be a series of negative cashflows throughout
the specified term or until death, if earlier, followed by a large positive cashflow at
the end of the term (or death, if earlier). Depending on the terms of the policy, the
amount payable on death may not be the same as that payable on survival.
   From the perspective of the insurer, there is a stream of regular positive cashflows
which cease at a specified point (or earlier, if the policyholder dies) followed by a large
negative cashflow. The negative cashflow is certain to be paid, but the timing of that
payment depends on whether/when the policyholder dies.

Term Assurance: A term assurance is an insurance policy which provides a lump
sum benefit on death before the end of a specified term usually in return for a series
1.6 Generalised cashflow model                                                          24


of regular premiums.
   The cashflows for the policyholder will be a series of negative cashflows throughout
the specified term or until death (or one negative cashflow at inception if paid on a
lump sum basis), if earlier, followed by a large positive cashflow payable on death, if
death occurs before the end of the term. If the policyholder survives to the end of the
term, there is no positive cashflow.
   From the perspective of the insurer, there is a stream of regular positive cashflows
which cease at a specified point (or earlier, if the policyholder dies) followed by a large
negative cashflow, contingent on policyholder death during the term.
   Generally, the negative cashflow (death benefit), if it occurs, is significantly higher
than the positive cashflow (premiums), when compared to, say, a pure endowment.
This is because, for each individual policy, the probability of the benefit being paid
is generally lower than for endowments because it is contingent on death, rather than
on survival.

Contingent Annuity: This is a similar contract to the annuity certain but the
payments are contingent upon certain events, such as survival, hence the payment
term for the regular cashflows (which will be negative from the perspective of the
annuity provider) is uncertain.
   Typical examples of contingent annuities include:

   • A single life annuity-where the regular payments made to the annuitant are
      contingent on the survival of that annuitant.

   • A joint life annuity-which covers two lives, where the regular payments are
      contingent on the survival of one or both of those lives.

   • A reversionary annuity-which is based on two lives, where the regular pay-
      ments start on the death of the first life if, and only if, the second life is alive
      at the time. Payments then continue until the death of the second life.

Car Insurance: A typical car insurance contract lasts for one year. In return for a
premium that can be paid as a single lump sum or at monthly intervals, the insurer
will provide cover to pay for damage to the insured vehicle or fire or theft of the
vehicle, known as ’property cover’. In many countries, such as the UK, the contract
also provides cover for compensation payable to third parties for death, injury, or
damage to their property, known as ’liability cover’.
   Depending on the terms of the policy, the insurance company may settle claims
directly with the policyholder or with another party. For example, in the case of theft
or total loss, the insurance company may pay a lump sum to the policyholder in lieu
1.6 Generalised cashflow model                                                         25


of that loss. In the case of damage to the insured vehicle, the insurance company may
settle the claim directly with the party undertaking the repairs without involving the
policyholder. In the case of third-party liability claims, the insurance company may
settle the claims directly with the third party.
   In some cases, the policyholder may be required to cover the cost of damage or
repairs first before the insurance company settles the claim, in which case the insurance
company will pay the policyholder directly. The cashflows for the policyholder will
usually be a single negative cashflow at the beginning of the year. Further cashflows
only take place in the event of a claim. If the policyholder has to pay for repairs
or compensation, this will incur a further negative cashflow, followed by a positive
cashflow when the insurance company settles the claim. If the insurance company
settles the claim directly with the repair company or third party, the policyholder
may not experience further cashflows.
   From the insurer’s perspective, there will be a positive cashflow at the beginning
of the policy, followed by a negative cashflow when the claim is settled. The timing
of the cashflows will depend on how long the claim takes to be reported and settled.
Typically, property claims take less time to settle than liability claims. Where liability
claims involve disputes, for example, necessitating court judgments, they can take
years to settle and the amounts are less certain. Cashflows tend to be short-term and
are payable within the year.

Health Cash Plan: A typical health insurance contract lasts for one year. In return
for a premium, the policyholder is entitled to benefits which may include hospital
treatment either paid for in full or in part, and/or cash benefits in lieu of treatment,
such as a fixed sum per day spent in the hospital as an in-patient.
   From the policyholder’s perspective, the cashflows will include a negative cashflow
at the beginning of the year followed by positive cashflows in the event of a claim in
the case of a cash benefit. Where the insurance company pays for hospital treatment
directly, the policyholder may experience no more cashflows after paying the initial
premium.
   From the perspective of the insurer, there will be an initial positive cashflow at
the start of the policy followed by negative cashflows in the event of a claim, when
those claims are settled.
   Cashflows tend to be short-term and are payable within the year.



