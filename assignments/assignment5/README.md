# Homework Assignment #5

## Date: 26-05-25

## Due date: 09-06-25, 15:00

**Do not change the signature (definition) of the functions in the exercise.**

**Tests are run with `pytest`.**

**Check the new submission guidelines below**

The data available in `data.json` is a table of participants in a questionnaire-type experiment. The data is mostly fine, but upon a closer inspection you may identify a few missing\corrupt values here and there. Our goal is to clean the data and analyze the results. Define a class that have several methods that process the given data. The first are:

```python
class QuestionnaireAnalysis:
    """
    Reads and analyzes data generated by the questionnaire experiment.
    Should be able to accept strings and pathlib.Path objects.
    """

    def __init__(self, data_fname: Union[pathlib.Path, str]):
        # ...

    def read_data(self):
        """Reads the json data located in self.data_fname into memory, to
        the attribute self.data.
        """
        # ...
```

The following questions should be answered by writing additional method(s) that perform the needed computation. The tests load the ground truth from the repo and check that your resulting values are identical to it.

1. Plot the distribution of ages of the participants. The bins for the histogram should be [0, 10), [10, 20), [20, 30), ..., [90, 100]. The function should return the result.

   ```python
   def show_age_distrib(self) -> Tuple[np.ndarray, np.ndarray]:
       """Calculates and plots the age distribution of the participants.

   Returns
   -------
   hist : np.ndarray
     Number of people in a given bin
   bins : np.ndarray
     Bin edges
       """
   ```

2. Participants without a valid email are useless since we can't contact them. Remove all of the rows with an invalid address and return the new DataFrame.
   A valid email address is one that follows these conditions:
   - Contains exactly one "@" sign, but doesn't start or end with it.
   - Contains a "." sign, but doesn't start or end with it.
   - The letter following the "@" sign (i.e, appears after it) must not be ".".

You're obviously encouraged to think of other email-defining conditions.

```python
def remove_rows_without_mail(self) -> pd.DataFrame:
    """Checks self.data for rows with invalid emails, and removes them.

Returns
-------
df : pd.DataFrame
  A corrected DataFrame, i.e. the same table but with the erroneous rows removed and
  the (ordinal) index after a reset.
    """
```

3. Some participants haven't answered all of the question. It was decided that the grade for those missing questions will be the average grade of the other question for that subject. Write a method that works on the original DataFrame (in `self.data`), replaces the missing values with the mean for that subject in the other questions and returns the corrected DataFrame as well as a `np.array` of the indices of the rows that were corrected.

   ```python
   def fill_na_with_mean(self) -> Tuple[pd.DataFrame, np.ndarray]:
       """Finds, in the original DataFrame, the subjects that didn't answer
       all questions, and replaces that missing value with the mean of the
       other grades for that student.

   Returns
   -------
   df : pd.DataFrame
     The corrected DataFrame after insertion of the mean grade
   arr : np.ndarray
         Row indices of the students that their new grades were generated
       """
   ```

4. Each participants should receive an integer score for his or her answers, given in a new "score" column you should add. After some deliberation it was decided that if a subject has no grade in two questions or more, the score of that subject will be NA. Write a method that produces this score by averaging the grades of the not-NaN questions in the relevant rows.

   ```python
   def score_subjects(self, maximal_nans_per_sub: int = 1) -> pd.DataFrame:
       """Calculates the average score of a subject and adds a new "score" column
       with it.

       If the subject has more than "maximal_nans_per_sub" NaN in his grades, the
       score should be NA. Otherwise, the score is simply the mean of the other grades.
       The datatype of score is UInt8, and the floating point raw numbers should be
       rounded down.

       Parameters
       ----------
       maximal_nans_per_sub : int, optional
           Number of allowed NaNs per subject before giving a NA score.

       Returns
       -------
       pd.DataFrame
           A new DF with a new column - "score".
       """
   ```

5. **BONUS 15 POINTS** There's reason to believe that there's a correlation between the subject's gender, age and grades.

   a. Use the original DataFrame and transform its index into a MultiIndex with three levels: the ordinal index (row number), gender and age.

   b. Allocate the different subjects into groups based on two parameters: Their gender, and whether their age is above or below 40. Hint - use `df.groupby`. The result should be similar to what is shown in the figure below (you don't have to plot it yourself).

   c. Return the DataFrame containing the average result per question per group.

   NOTE: Due to an error on my behalf, this question may be submitted by Thursday night, 21.5 at 23:59.

   ```python
   def correlate_gender_age(self) -> pd.DataFrame:
       """Looks for a correlation between the gender of the subject, their age
       and the score for all five questions.

   Returns
   -------
   pd.DataFrame
       A DataFrame with a MultiIndex containing the gender and whether the subject is above
       40 years of age, and the average score in each of the five questions.
   """
   ```

   [Average per group - result of `correlate_gender_age`](avg_per_group.png)

## Submission

The submission will be done via a pull request to this repository. A pull request is a common action when using Git and GitHub, and it represents the mechanism by which two or more programmers work on the same codebase. This operation pings the owner of the repository, i.e. the main code author, presenting changes that you think should be done to the code inside that repository.

Contributions to most open-source projects, from tiny command-line utilities to the Linux operating systems, are done using pull requests. You can read more about them [here](https://help.github.com/en/articles/about-pull-requests), and I've also given more details and examples during class 7.

To start off, fork the `hw5` repository by clicking the button on the top right-hand side. This will create a "snapshot" of the main repository, by copying its current state into a new repository under your control. You should clone this new repo into your computer, and work as usual - add files, commit and push as you normally would. When you're done , i.e. uploaded the final files to GitHub, go to your repo and click the "new pull request" button and create it. You can update the pull request after it was created by simply pushing new updates to your own original fork, so starting a pull request doesn't forbid you from updating your code. If you're unsure whether the operation was successful, go back to the original repo I started and click the "Pull Requests" option at the top of the page. Your PR should be listed there. The deadline for that PR to show in my repo is the deadline of submission.
