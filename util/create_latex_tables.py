from collections import defaultdict
import numpy as np
acc_mean, acc_std = 'acc_mean', 'acc_std'
auc_mean, auc_std = 'auc_mean', 'auc_std'
mcc_mean, mcc_std = 'mcc_mean', 'mcc_std'

'''
Results Rawi
'''
str_antibodies_rawi = '	b12	4E10	2F5	2G12	VRC01	PG9	PGT121	PGT128	PGT145	3BNC117	PG16	10-1074	PGDM1400	VRC26.08	VRC26.25	VRC13	VRC03	VRC-PG04	35O22	NIH45-46	VRC-CH31	8ANC195	HJ16	PGT151	VRC38.01	CH01	PGT135	DH270.1	DH270.5	DH270.6	VRC29.03	VRC34.01	VRC07'
str_acc_rawi = '0.79 (0.01)	0.94 (0)	0.95 (0)	0.91 (0.01)	0.92 (0)	0.86 (0.01)	0.88 (0.01)	0.86 (0.01)	0.86 (0.02)	0.9 (0.01)	0.84 (0.01)	0.94 (0.01)	0.89 (0)	0.85 (0.01)	0.87 (0.01)	0.88 (0.01)	0.81 (0.02)	0.87 (0.01)	0.66 (0.02)	0.89 (0.01)	0.87 (0.01)	0.89 (0.02)	0.66 (0.02)	0.83 (0.01)	0.87 (0.03)	0.77 (0.03)	0.74 (0.02)	0.9 (0.02)	0.91 (0.01)	0.93 (0.01)	0.84 (0.01)	0.79 (0.03)	0.93 (0.01)'
str_auc_rawi = '0.82 (0.01)	0.82 (0.02)	0.97 (0)	0.93 (0)	0.89 (0.01)	0.85 (0.01)	0.92 (0)	0.89 (0.01)	0.86 (0.02)	0.88 (0.02)	0.79 (0.02)	0.95 (0.01)	0.83 (0.02)	0.89 (0.01)	0.89 (0.01)	0.83 (0.01)	0.83 (0.02)	0.78 (0.05)	0.63 (0.02)	0.8 (0.02)	0.78 (0.03)	0.9 (0.03)	0.67 (0.02)	0.78 (0.02)	0.87 (0.02)	0.77 (0.02)	0.77 (0.02)	0.92 (0.02)	0.93 (0.02)	0.93 (0.01)	0.82 (0.02)	0.78 (0.03)	0.78 (0.05)'
str_mcc_rawi = '0.56 (0.02)	0.63 (0.02)	0.89 (0.01)	0.75 (0.01)	0.7 (0.02)	0.61 (0.02)	0.75 (0.01)	0.72 (0.01)	0.67 (0.04)	0.69 (0.03)	0.57 (0.04)	0.86 (0.01)	0.66 (0.02)	0.7 (0.02)	0.71 (0.04)	0.63 (0.03)	0.61 (0.03)	0.57 (0.05)	0.38 (0.04)	0.59 (0.05)	0.6 (0.06)	0.77 (0.04)	0.42 (0.03)	0.58 (0.03)	0.7 (0.05)	0.56 (0.04)	0.54 (0.01)	0.82 (0.03)	0.83 (0.02)	0.85 (0.02)	0.64 (0.02)	0.61 (0.05)	0.66 (0.04)'

antibodies_rawi = str_antibodies_rawi.split()
acc_rawi = str_acc_rawi.split()
auc_rawi = str_auc_rawi.split()
mcc_rawi = str_mcc_rawi.split()

results_rawi = defaultdict(dict)

for i in range(len(antibodies_rawi)):
    ab = antibodies_rawi[i]
    results_rawi[ab][acc_mean] = float(acc_rawi[i * 2])
    results_rawi[ab][acc_std] = float(acc_rawi[i * 2 + 1][1:-1])
    results_rawi[ab][auc_mean] = float(auc_rawi[i * 2])
    results_rawi[ab][auc_std] = float(auc_rawi[i * 2 + 1][1:-1])
    results_rawi[ab][mcc_mean] = float(mcc_rawi[i * 2])
    results_rawi[ab][mcc_std] = float(mcc_rawi[i * 2 + 1][1:-1])

'''
Results FC-ATT-GRU
'''
str_header = 'Run ID,Name,Source Type,Source Name,User,Status,cv_folds_trim,n_trials,prune_trehold,cv mean acc 10-1074,cv mean acc 2F5,cv mean acc 2G12,cv mean acc 35O22,cv mean acc 3BNC117,cv mean acc 4E10,cv mean acc 8ANC195,cv mean acc CH01,cv mean acc DH270.1,cv mean acc DH270.5,cv mean acc DH270.6,cv mean acc HJ16,cv mean acc NIH45-46,cv mean acc PG16,cv mean acc PG9,cv mean acc PGDM1400,cv mean acc PGT121,cv mean acc PGT128,cv mean acc PGT135,cv mean acc PGT145,cv mean acc PGT151,cv mean acc VRC-CH31,cv mean acc VRC-PG04,cv mean acc VRC01,cv mean acc VRC03,cv mean acc VRC07,cv mean acc VRC26.08,cv mean acc VRC26.25,cv mean acc VRC34.01,cv mean acc VRC38.01,cv mean acc b12,cv mean auc 10-1074,cv mean auc 2F5,cv mean auc 2G12,cv mean auc 35O22,cv mean auc 3BNC117,cv mean auc 4E10,cv mean auc 8ANC195,cv mean auc CH01,cv mean auc DH270.1,cv mean auc DH270.5,cv mean auc DH270.6,cv mean auc HJ16,cv mean auc NIH45-46,cv mean auc PG16,cv mean auc PG9,cv mean auc PGDM1400,cv mean auc PGT121,cv mean auc PGT128,cv mean auc PGT135,cv mean auc PGT145,cv mean auc PGT151,cv mean auc VRC-CH31,cv mean auc VRC-PG04,cv mean auc VRC01,cv mean auc VRC03,cv mean auc VRC07,cv mean auc VRC26.08,cv mean auc VRC26.25,cv mean auc VRC34.01,cv mean auc VRC38.01,cv mean auc b12,cv mean mcc 10-1074,cv mean mcc 2F5,cv mean mcc 2G12,cv mean mcc 35O22,cv mean mcc 3BNC117,cv mean mcc 4E10,cv mean mcc 8ANC195,cv mean mcc CH01,cv mean mcc DH270.1,cv mean mcc DH270.5,cv mean mcc DH270.6,cv mean mcc HJ16,cv mean mcc NIH45-46,cv mean mcc PG16,cv mean mcc PG9,cv mean mcc PGDM1400,cv mean mcc PGT121,cv mean mcc PGT128,cv mean mcc PGT135,cv mean mcc PGT145,cv mean mcc PGT151,cv mean mcc VRC-CH31,cv mean mcc VRC-PG04,cv mean mcc VRC01,cv mean mcc VRC03,cv mean mcc VRC07,cv mean mcc VRC26.08,cv mean mcc VRC26.25,cv mean mcc VRC34.01,cv mean mcc VRC38.01,cv mean mcc b12,cv std acc 10-1074,cv std acc 2F5,cv std acc 2G12,cv std acc 35O22,cv std acc 3BNC117,cv std acc 4E10,cv std acc 8ANC195,cv std acc CH01,cv std acc DH270.1,cv std acc DH270.5,cv std acc DH270.6,cv std acc HJ16,cv std acc NIH45-46,cv std acc PG16,cv std acc PG9,cv std acc PGDM1400,cv std acc PGT121,cv std acc PGT128,cv std acc PGT135,cv std acc PGT145,cv std acc PGT151,cv std acc VRC-CH31,cv std acc VRC-PG04,cv std acc VRC01,cv std acc VRC03,cv std acc VRC07,cv std acc VRC26.08,cv std acc VRC26.25,cv std acc VRC34.01,cv std acc VRC38.01,cv std acc b12,cv std auc 10-1074,cv std auc 2F5,cv std auc 2G12,cv std auc 35O22,cv std auc 3BNC117,cv std auc 4E10,cv std auc 8ANC195,cv std auc CH01,cv std auc DH270.1,cv std auc DH270.5,cv std auc DH270.6,cv std auc HJ16,cv std auc NIH45-46,cv std auc PG16,cv std auc PG9,cv std auc PGDM1400,cv std auc PGT121,cv std auc PGT128,cv std auc PGT135,cv std auc PGT145,cv std auc PGT151,cv std auc VRC-CH31,cv std auc VRC-PG04,cv std auc VRC01,cv std auc VRC03,cv std auc VRC07,cv std auc VRC26.08,cv std auc VRC26.25,cv std auc VRC34.01,cv std auc VRC38.01,cv std auc b12,cv std mcc 10-1074,cv std mcc 2F5,cv std mcc 2G12,cv std mcc 35O22,cv std mcc 3BNC117,cv std mcc 4E10,cv std mcc 8ANC195,cv std mcc CH01,cv std mcc DH270.1,cv std mcc DH270.5,cv std mcc DH270.6,cv std mcc HJ16,cv std mcc NIH45-46,cv std mcc PG16,cv std mcc PG9,cv std mcc PGDM1400,cv std mcc PGT121,cv std mcc PGT128,cv std mcc PGT135,cv std mcc PGT145,cv std mcc PGT151,cv std mcc VRC-CH31,cv std mcc VRC-PG04,cv std mcc VRC01,cv std mcc VRC03,cv std mcc VRC07,cv std mcc VRC26.08,cv std mcc VRC26.25,cv std mcc VRC34.01,cv std mcc VRC38.01,cv std mcc b12,global_acc,global_auc,global_mcc,corrections,freeze,input,model,pretrain_epochs,prune,splits,trial'
str_data = 'd83addff4bde47d79b9a09773d1f5a96,,LOCAL,/opt/conda/lib/python3.7/site-packages/ipykernel_launcher.py,root,FINISHED,10,300,0.05,0.960418118466899,0.9156738366988587,0.8892085029398461,0.7375132275132275,0.9353961352657006,0.9331343283582091,0.7844301994301994,0.8683152173913042,0.9483809523809525,0.9799761904761906,0.9615,0.7458615384615382,0.9634757834757834,0.8856976744186048,0.922936879018118,0.9389024390243903,0.9237607843137254,0.9027176470588237,0.8470289855072463,0.8754285714285713,0.8794307692307693,0.9247435897435899,0.932247311827957,0.9546875,0.8862215909090909,0.9358605974395446,0.9670548780487803,0.9366591591591593,0.7558095238095238,0.8747999999999999,0.7904244913928012,0.9838653083746343,0.9407318318669384,0.8873857257817768,0.7250799563977638,0.9240869921434738,0.7825480762605427,0.7589671252226027,0.8925636010088409,0.9599637673834103,0.9925280083012226,0.9772359066859068,0.6821977510322358,0.9550827236074376,0.896867576905946,0.9323610289740303,0.9511688565775106,0.9484495129665893,0.9293431829388052,0.8563183052757356,0.8880536076176816,0.8681402319935292,0.9040545946962044,0.9527763137934191,0.9460702220263291,0.9099530282389672,0.9132249018020013,0.9838785210034547,0.9648862068458505,0.7265002041609185,0.8353239134122988,0.7909022429521848,0.9167658528795457,0.8321962535075574,0.6713185557042647,0.5121063756791533,0.8073568778530813,0.599422910816045,0.5679142856814663,0.7466227518515431,0.900731118900083,0.9608177853443209,0.9264707365796241,0.45161786340766474,0.8701775494540415,0.7366597278370096,0.8061113569088222,0.8389065290920081,0.8434874507637666,0.804317737889061,0.6922650998893455,0.7257657438173206,0.7350409839278366,0.7716987909318594,0.807810961269547,0.8400581618958155,0.7744373666085181,0.7965731378296347,0.9327905336103137,0.8623620406132879,0.5364526571258634,0.6895699782517859,0.5306326376192991,0.027684300325517636,0.03410041577352585,0.04518447301160067,0.0693596912900147,0.035223709697414354,0.03051971004735468,0.07536785301812128,0.05204839407788636,0.04725801231422198,0.029308150522931856,0.04219065758318525,0.09584299167521033,0.03516789083258271,0.0509978654076209,0.03335597465591631,0.03539790389610595,0.034055841923065294,0.037533376355428194,0.06481575198610326,0.05090331052175424,0.07436823620480063,0.07135971745949345,0.03984694239663194,0.02248046026552837,0.045796413058307485,0.1668250211040049,0.027079412458906334,0.038212498592113224,0.07775427892506279,0.06423363604841315,0.044673390750460895,0.01535207238593427,0.0323730106989747,0.05733685212214779,0.09974555470083607,0.052259938566059205,0.1194864731250459,0.11196609879309483,0.05757825191551064,0.04526050226094917,0.015637578720376775,0.03518583805888674,0.10653211057257092,0.0705881129510166,0.05184663102556973,0.035349853738813546,0.03681216675124864,0.032152761624994745,0.03837482846072956,0.07591201450941482,0.060340515147974526,0.09074855759683248,0.0858979960576818,0.04664598732952812,0.04043096643027224,0.051706612526651465,0.18271488663765043,0.019806744934256687,0.02984506380785737,0.11043409263978918,0.10521194419506098,0.055629827730188826,0.05671518240753204,0.0670945275559903,0.110112038342622,0.10681510959427665,0.09710526484966772,0.13668396285497025,0.13191598719403627,0.09701054808535306,0.08834756395353742,0.05642338230820896,0.07845768857527383,0.1391303598482648,0.12362572678511848,0.10463818638806438,0.0800543176894642,0.08906167361894417,0.06758074272605556,0.07312598961576762,0.12425902457250533,0.10715969104261794,0.15090133407035514,0.16162576992995178,0.11730644206408457,0.07343559813927462,0.08829507438440246,0.19204750914633342,0.055395991339938645,0.08204816164073195,0.1227648646650381,0.14882389422296344,0.07532373006392556,0.895409562038368,0.8922744911692981,0.7576922520496608,gaps and amino acids and padding,antb and embed,props-only,fc_att_gru_1_layer,100,treshold 0.05,uniform,252'

header = str_header.split(',')
data = str_data.split(',')

results_fc_att_gru = defaultdict(dict)

for i, txt in enumerate(header):
    ab = txt.split()[-1]
    if 'cv mean acc' in txt:
        results_fc_att_gru[ab][acc_mean] = float(data[i])
    elif 'cv mean auc' in txt:
        results_fc_att_gru[ab][auc_mean] = float(data[i])
    elif 'cv mean mcc' in txt:
        results_fc_att_gru[ab][mcc_mean] = float(data[i])
    elif 'cv std acc' in txt:
        results_fc_att_gru[ab][acc_std] = float(data[i])
    elif 'cv std auc' in txt:
        results_fc_att_gru[ab][auc_std] = float(data[i])
    elif 'cv std mcc' in txt:
        results_fc_att_gru[ab][mcc_std] = float(data[i])

def display_table_row(ab, metrics):
    table_row = f'{ab} & {str(metrics[0])[:4]}({round(metrics[1], 2)}) & ' + \
                f'{str(metrics[2])[:4]}({round(metrics[3], 2)}) & ' + \
                f'{str(metrics[4])[:4]}({round(metrics[5], 2)}) & ' + \
                f'{str(metrics[6])[:4]}({round(metrics[7], 2)}) & ' + \
                f'{str(metrics[8])[:4]}({round(metrics[9], 2)}) & ' + \
                f'{str(metrics[10])[:4]}({round(metrics[11], 2)})\\\\'
    return table_row

totals = np.zeros(12)
for ab, metrics_us in results_fc_att_gru.items():
    metrics_Rawi = results_rawi[ab]
    metrics = np.array([
        metrics_Rawi[mcc_mean], metrics_Rawi[mcc_std],
        metrics_Rawi[auc_mean], metrics_Rawi[auc_std],
        metrics_Rawi[acc_mean], metrics_Rawi[acc_std],
        metrics_us[mcc_mean], metrics_us[mcc_std],
        metrics_us[auc_mean], metrics_us[auc_std],
        metrics_us[acc_mean], metrics_us[acc_std]
    ])
    totals = totals + metrics
    print(display_table_row(ab, metrics))
totals = totals / len(results_fc_att_gru)
print(display_table_row('Average', totals))