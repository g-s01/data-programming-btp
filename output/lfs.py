lf1_80704351817598 = lambda sentence, coarse_labels, possible_fine_labels: [possible_fine_labels.get(label, 'O') for label in coarse_labels if (label == 'Facility' or label in ['HumanSettlement', 'Station']) and any(fine_label in sentence for fine_label in possible_fine_labels)]

lf2_8220802996125903 = lambda sentence, coarse_labels, possible_fine_labels: [fine_label if label in possible_fine_labels else 'O' for label in coarse_labels for fine_label in sentence]

