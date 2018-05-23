import sys
import csv
import pandas as pd

df_rand = pd.read_csv('smith_rand.csv')
df_covar = pd.read_csv('smith_covariates.csv')
df_outc = pd.read_csv('smith_outcomes.csv')

df_rc_merge = pd.merge(df_covar, df_rand, on='ai_id')

def df_join_inner(dfL, dfR):
	inner = dfL.join(dfR, on='ai_id', how='inner', lsuffix='_left', rsuffix='_right')
	return inner

def df_join(dfL, dfR):
	inner = dfL.join(dfR, on='ai_id', how='inner', lsuffix='_left', rsuffix='_right')
	outer = dfL.join(dfR, on='ai_id', how='outer', lsuffix='_left', rsuffix='_right')
	lefto = dfL.join(dfR, on='ai_id', how='left', lsuffix='_left', rsuffix='_right')
	righto = dfL.join(dfR, on='ai_id', how='right', lsuffix='_left', rsuffix='_right')

	df_array = [inner, lefto, righto, outer]
	return df_array

def bin_arg(df_rc):
	df_age = [pd.DataFrame(df_rc[(df_rc.age >= 18) & (df_rc.age <= 34)]), pd.DataFrame(df_rc[(df_rc.age >= 35) & (df_rc.age <= 44)]), pd.DataFrame(df_rc[(df_rc.age >= 45) & (df_rc.age <= 64)]), pd.DataFrame(df_rc[df_rc.age >= 65])]
	df_race = [pd.DataFrame(df_rc[df_rc.race == 'caucausion']), pd.DataFrame(df_rc[df_rc.race == 'black']), pd.DataFrame(df_rc[df_rc.race == 'hispanic']), pd.DataFrame(df_rc[(df_rc.race == 'asian') | (df_rc.race == 'middleEastern') | (df_rc.race == 'unknown')])]
	df_gender =[pd.DataFrame(df_rc[df_rc.gender == 'male']), pd.DataFrame(df_rc[df_rc.gender == 'female']), pd.DataFrame(df_rc[df_rc.gender == 'NaN'])]
	return df_age, df_race, df_gender

def main():

	df_a, df_r, df_g = bin_arg(df_rc_merge)

	#df_join_array = df_join(df_covar, df_rand)
	jinner = df_join_inner(df_covar, df_rand)
	print(jinner)
	print(jinner.count)

if __name__ == "__main__":main()

"""
EXAMPLES

# List column names
df_covar.columns

# Working join
df_rc_join = df_covar.join(df_rand, on='ai_id', how='inner', lsuffix='_left', rsuffix='_right')

"""
