import matplotlib.pyplot as plt
import numpy as np

def loss_recall_plot(train_log, suptitle):
    
    num_epochs = np.arange(1, len(train_log['loss'])+1)

    fig, axes = plt.subplots(1, 2, figsize=(17, 5))

    axes[0].plot(num_epochs, train_log['loss'], label='train loss', color='green')
    axes[0].plot(num_epochs, train_log['val_loss'], label='validation loss', color='red')
    axes[0].set_ylabel('loss')
    axes[0].legend()
    axes[0].grid()

    axes[1].plot(num_epochs, train_log['recall'], label='train recall', color='green')
    axes[1].plot(num_epochs, train_log['val_recall'], label='validation recall', color='red')
    axes[1].set_ylabel('recall')
    axes[1].legend()
    axes[1].grid()

    for ax in axes:
        ax.set_xlabel('# epochs')

    fig.suptitle(suptitle, fontsize=16);