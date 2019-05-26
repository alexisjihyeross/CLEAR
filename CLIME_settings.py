from tkinter import *
import sys

""" Specify input parameters """
def init(evaluation_type):
    global case_study, max_predictors, first_obs,last_obs, num_samples, regression_type,\
    score_type, test_sample, regression_sample_size, min_target_sample,\
    feature_with_indicator,LIME_path, with_indicator_feature, indicator_threshold,\
    neighbourhood_algorithm,perturb_one_feature,only_feature_perturbed,\
    apply_counterfactual_weights,counterfactual_weight,exclude_infeasible_perturbations,\
    generate_regression_files,LIME_comparison,interactions_only, no_centering,no_polynomimals 
    
    case_study = 'Credit Card' # 'Census','PIMA Indians Diabetes','Credit Card','BreastC'
    max_predictors = 15  # maximum number of dependent variables in stepwise regression
    first_obs =1
    last_obs=100  # number of observations to analyse in CLIME test dataset Census 115/225 in test1 PIMA 115 in test1
    # Credit 104
    num_samples=50000 # number of observations to generate in Synthetic Dataset. Defaul 100000
    regression_type = 'multiple' #'multiple' 'logistic'
    score_type = 'adjR' # prsquared is McFadden Pseudo R-squared. Can also be 
    #                          set to aic or adjR (adjusted R-squared)
    test_sample=1            # sets CLIME's test dataset
    regression_sample_size =200   # minimum number of observations in local regression. Default 200
    feature_with_indicator = 'Glucose'  #age,Glucose
    LIME_path='D:/LIME/' #'D:/LIME/''/content/drive/My Drive/Colab/'
    with_indicator_feature = False    # whether to use this indicator variable
    indicator_threshold = 1.5  # threshold for indicator variable # for PAY 0 0=0.1, 1 =0.91
    neighbourhood_algorithm= 'L3' #default is L3 . Tested against Unbalanced
    perturb_one_feature = False # perturb only one feature eg 'age'
    only_feature_perturbed = 'age' # the single feature that is perturbed if
                                   # 'perturb_one_feature' = True 
    interactions_only = False
    no_centering = True #applies only to logistic regression
    no_polynomimals = False
    exclude_infeasible_perturbations = False                               
    apply_counterfactual_weights = False
    counterfactual_weight = 9 # default to 9
    generate_regression_files = False
    LIME_comparison = False                         
    #check for inconsistent input data
    check_input_parameters(evaluation_type)

""" Check if input parameters are consistent"""
def check_input_parameters(evaluation_type):

    def close_program(): 
            root.destroy()
            sys.exit()
    
    error_msg = ""   
    if perturb_one_feature == True and case_study != 'Census':
        error_msg = "'Perturb_one_feature' only applies to 'Census' dataset"
    elif perturb_one_feature == False and case_study == 'Census':
        error_msg = "'Perturb_one_feature' currently needs to apply to 'Census' dataset"  
    elif perturb_one_feature == True and only_feature_perturbed  != 'age':
        error_msg = "'Only feature perturbed' should be set to age"    
    elif regression_type == 'logistic' and   score_type == 'adjR':
        error_msg = "Adjusted R squared cannot be used with logistic regression"
    elif regression_type == 'multiple' and   score_type == 'prsquared':
        error_msg = "McFadden Pseudo R-squared cannot be used with multiple regression"
    elif case_study not in ['Census','PIMA Indians Diabetes','Credit Card','BreastC'] :
        error_msg = "Case study incorrectly specified"
    elif regression_type not in ['multiple', 'logistic']:
        error_msg = "Regression type misspecified"    
    elif LIME_comparison == True and  regression_type != 'multiple' :
        error_msg = "LIME comparison only works with multiple regression"    
    elif evaluation_type == 'CLIME' and LIME_comparison == True:
        error_msg = "LIME comparison called from CLIME module"  
    elif evaluation_type == 'LIME_evaluate' and LIME_comparison == False:
        error_msg = "LIME comparison not set to True"       
        
    if  error_msg != "":    
        root=Tk()
        root.title("Input Error in CLIME_settings")
        root.geometry("350x150")

        label_1 = Label(root,text =error_msg, \
                        justify = CENTER, height = 4, wraplength = 150)
        button_1 = Button(root, text= "OK", \
                          padx = 5, pady = 5, command = close_program)
        label_1.pack()
        button_1.pack()
        root.attributes("-topmost", True)
        root.focus_force() 
        root.mainloop()
    

#    