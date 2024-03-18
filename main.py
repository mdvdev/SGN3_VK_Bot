from VkBot import VkBot

GROUP_ID = '224997570'
GROUP_TOKEN = 'vk1.a.3H_djNkc1xsYGudI63vh2ZQ_eIfmFxd-B-KKhpElILp-V093JBvQtOp4FEMY0P5t3G3XxHlaStqCmee5bLo44LfGby-Q0RyCDO8NluUcnBql1iUZ2VZUXsbNVX6A0w0d-SSDdLIz5zjqg_p_2M0u9NboIXMqymvt9_MIgNGrcQOLqr4wWtuhxbFUR3OY3ZqmzS0axA6W1OaJB9-igZxgbg'


def main():
    vk_bot = VkBot(GROUP_ID, GROUP_TOKEN)
    vk_bot.start()


if __name__ == '__main__':
    main()
