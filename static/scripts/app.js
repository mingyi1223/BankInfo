function bankSearch ($el){
        const banks = JSON.parse($el.dataset.banks);
        const branches = JSON.parse($el.dataset.branches);
        const selectedBank = $el.dataset.selectedBank ? JSON.parse($el.dataset.selectedBank) : null;
        const selectedBranch = $el.dataset.selectedBranch ? JSON.parse($el.dataset.selectedBranch) : null;

        console.log("123")
        

        return {
            searchbank: '',
            searchbranch: '',
            banks: banks,
            branches: branches,
            selectedBankCode: selectedBank ? selectedBank.code : '',
            selectedBank: selectedBank || {},
            selectedBranch: selectedBranch || {},
            bankplaceholder: '請輸入關鍵字或銀行代碼',
            branchplaceholder: '請選擇分行名稱',
            showbank: false,
            showbranch: false,
            showDetail: selectedBank && selectedBranch ? true : false,
            copyCodeText: '複製代碼',
            copyButtonText: '複製此頁面連結',

            get filteredBanks() {
                return this.banks.filter(bank => bank.title.includes(this.searchbank) || bank.code.includes(this.searchbank));
            },
            get filteredBranches() {
                return this.branches.filter(branch => branch.bank_code === this.selectedBankCode && (branch.title.includes(this.searchbranch) || branch.code.includes(this.searchbranch)));
            },

            clearSearch() {
                this.searchbank = ''; 
                this.showbank = true;
            },
            clearBranchSearch() {
                this.searchbranch = ''; 
                this.showbranch = true;
            },
            selectBranch(branch) {
                this.selectedBranch = branch;
                this.searchbranch = branch.title;
                this.showbranch = false;
                this.showDetail = true;
            },
            selectBank(bank) {
                this.searchbank = `${bank.code} ${bank.title}`;
                this.selectedBankCode = bank.code;
                this.selectedBank = bank;
                this.showbank = false;
                this.searchbranch = '';
                this.selectedBranch = {};
                this.showDetail = false;
            },
            copyCode() {
                navigator.clipboard.writeText(this.selectedBranch.code).then(() => {
                    this.copyCodeText = '已複製';
                    setTimeout(() => {
                        this.copyCodeText = '複製代碼';
                    }, 2000);
                });
            },
            copyURL() {
                const url = `${window.location.origin}/${this.selectedBank.code}/${this.selectedBranch.code}/${this.selectedBank.title}-${this.selectedBranch.title}.html`;
                navigator.clipboard.writeText(url).then(() => {
                    this.copyButtonText = '已複製';
                    setTimeout(() => {
                        this.copyButtonText = '複製此頁面連結';
                    }, 2000);
                });
            },
        };
    };
