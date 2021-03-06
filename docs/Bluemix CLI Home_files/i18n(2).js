define({
		homeTitle: "Bluemix CLI ホーム",
		home: "ホーム",
		allVersions: "すべてのバージョン",
		pluginsRepo: "プラグイン・リポジトリー",
		bluemixCLI: "Bluemix CLI",
		currentVersion: "(現行バージョン: {{:latest}})",
		downloadForMac: "ダウンロード (Mac OS X 用)",
		downloadForLinux: "ダウンロード (Linux 64 ビット用)",
		downloadForWin: "ダウンロード (Windows 64 ビット用)",
		whatIsIt: "説明",
		whatIsItDesc_1: "Bluemix CLI は、コマンド・ライン・インターフェースを介して、Bluemix 内のアプリケーション、仮想サーバー、コンテナー、およびその他のコンポーネントと対話するための一元化された手法を提供します。また、特定の計算タイプと対話するときにも、Cloud Foundry、Docker、および OpenStack コミュニティーからコマンド・ライン・ツールを利用します。Bluemix CLI は、これらのコミュニティー・ツールが使用されている場合の環境設定の操作に役立ちます。",
		whatIsItDesc_2: "Bluemix CLI のコマンドは、構造上の全体像を提供できるように、名前空間で編成されています。Bash または Zsh を使用している場合、Bluemix CLI のオートコンプリート機能によってコマンドとその引数の候補が提示されるので、適宜選択して入力することができます。この機能により、正しいコマンドを簡単に検索して使用できます。",
		plugins: "プラグイン",
		pluginsDesc: "Cloud Foundry CLI と同様に、Bluemix CLI でも、組み込みコマンド以外の他のコマンドを追加するプラグイン拡張フレームワークをサポートしています。Bluemix には、Bluemix CLI プラグインと Cloud Foundry CLI プラグインの両方をホストするリポジトリーがあります。",
		
		// NOTE: Do NOT translate <a href=xxx target=xxx>
		cfPluginsRepo: "Cloud Foundry CLI 用のプラグインをホストする <a href=\"repository.html#cf-plugins\" target=\"_blank\">Cloud Foundry CLI プラグイン・リポジトリー</a>。",
		bxPluginsRepo: "Bluemix CLI 専用のプラグインをホストする <a href=\"repository.html#bluemix-plugins\" target=\"_blank\">Bluemix CLI プラグイン・リポジトリー。</a>これらのプラグインは、Bluemix CLI で提供される固有のフィーチャーを活用します。",
		moreInfo: "Bluemix CLI の組み込みコマンドについて詳しくは、Bluemix の資料の『<a href=\"https://www.ng.bluemix.net/docs/cli/downloads.html\" target=\"_blank\">コマンド・ライン・インターフェース</a>』を参照してください。",
			
		gettingStarted: "入門",
		gettingStartedDesc: "Bluemix CLI のインストールが完了すると、コマンド・シェルから Bluemix コマンドにアクセスできます。Bluemix アカウントの E メール・アドレスとパスワードを使用してログインしてください。以下に例を示します。",
		example: "これで Bluemix の組み込みコマンドを使用する準備ができました。以下に例を示します。",
		
		// NOTE: Do NOT translate <b>, </b>, <i> and </i>
		restrictions: "<b><i>制約事項</i>:</b> Bluemix CLI コマンド・ライン・インターフェースは Cygwin ではサポートされていません。Cygwin コマンド・ライン・ウィンドウ以外のコマンド・ライン・ウィンドウで Bluemix CLI を使用してください。",
		proxyNote: "<b><i>注</i>:</b> CLI および Bluemix が稼働しているホストとの間に HTTP プロキシー・サーバーがあるネットワークを使用している場合、HTTP_PROXY 環境変数を設定することによって、プロキシー・サーバーのホスト名または IP アドレスを指定する必要があります。",
		howToInstallBx: "Bluemix CLI のインストール方法",
		cfRequired: "Bluemix CLI をインストールする前に、ご使用のシステムに Cloud Foundry コマンド・ライン・インターフェース (CLI を参照) がインストール済みであることを確認してください。",
		installOnMacWin: "Mac OS および Windows の場合は、パッケージをダウンロードしてインストーラーを実行します。",
		installOnLinux: "Linux の場合、以下のステップを実行してください。",
		unzipInstaller: "パッケージをダウンロードして、展開します。以下に例を示します。",
		installWithRootPerm: "「Bluemix_CLI」ディレクトリーに移動し、root 権限で (「sudo」または root ユーザーで)、「./install_bluemix_cli」を実行します。以下に例を示します。",
		howToInstallPlugin: "プラグインのインストール方法",
		installLocally: "ローカルからインストールする場合、以下のステップを実行してください。",
		downloadPlugin: "プラグインをダウンロードします。以下に例を示します。",
		chmodForUnix: "UNIX 系システムの場合、「chmod」コマンドを使用して、ダウンロードしたファイルを実行可能にする必要があります。以下に例を示します。",
		installPluginLocally: "「bluemix plugin install」コマンドを使用してプラグインをインストールします。以下に例を示します。",
		installRemotely: "リモート・サーバーからインストールするには、次のようにします。",
		installPluginRemotely: "「bluemix plugin install」コマンドを使用して、リモート URL から直接プラグインをインストールします。",
		installFromRepo: "リポジトリーからインストールする場合、以下のステップを実行してください。",
		listRepoPlugins: "リポジトリー内でプラグインを見つけます。Bluemix CLI をインストールした後、オフィシャル・リポジトリー「Bluemix」がデフォルトで追加されます。「bluemix plugin repo-plugins」コマンドを使用して、「Bluemix」リポジトリー内のプラグインをリストできます。以下に例を示します。",
		installPluginFromRepo: "次に、「bluemix plugin install」コマンドを使用して、「Bluemix」リポジトリーからプラグインをインストールします。以下に例を示します。",
		
		allVersionsTitle: "Bluemix CLI の全バージョン",
		version: "バージョン",
		updated: "更新済み",
		commandsRef: "コマンド・リファレンス",
		commandsRefWithComma: "コマンド・リファレンス",
		reference: "リファレンス",
		referenceWithComma: "リファレンス:",
		documentWithComma: "文書:",
		macOS: "Mac OS",
		linux32: "Linux32",
		linux64: "Linux64",
		windows32: "Win32",
		windows64: "Win64",
		changeLog: "変更ログ",
		download: "ダウンロード",
		
		"0.3.0-desc-1": "コマンドおよび名前空間の再編成",
		"0.3.0-desc-2": "新規名前空間「app」および「service」",
		"0.3.0-desc-3": "「app」および「service」名前空間で頻繁に使用される cf コマンドのラップ",

		"0.3.1-desc-1": "カラフルなコンソール出力のサポート (Windows の場合)",
		"0.3.1-desc-2": "出力メッセージの軽微な改善",

		"0.3.2-desc-1": "Bluemix CLI インストーラーにバンドルされていた CF CLI の削除",
		"0.3.2-desc-2": "Linux 32 および Windows 32 プラットフォーム用のインストーラーのサポート",
		"0.3.2-desc-3": "コマンド「bluemix iam account-users」および「bluemix iam account-user-invite」の追加",
		"0.3.2-desc-4": "アカウント所有者による組織の作成および削除を有効化",
		"0.3.2-desc-5": "すべての地域からの組織の削除を有効化",
		"0.3.2-desc-6": "Bluemix と対話する際のユーザー名別の組織/スペースの役割設定における障害の修正",
		"0.3.2-desc-7": "Bluemix との対話時の組織/スペースの役割の照会における障害の修正",
		"0.3.2-desc-8": "エラー処理の改善",
		"0.3.2-desc-9": "curl API エンドポイントを Bluemix MCCP (Multi Cloud Control Proxy) に変更",
		"0.3.2-desc-10": "「bluemix vm rc-download」を一時的に無効化",
		"0.3.2-desc-11": "API 変更による「bluemix catalog template-run」コマンドの障害の修正",
		"0.3.2-desc-12": "プラグイン・コンテキスト内でのトークンのリフレッシュをサポート",
		"0.3.2-desc-13": "HTTP クライアント・ライブラリー内のトークンのリフレッシュをサポート",
		"0.3.2-desc-14": "プラグイン・コンテキスト内でのトレース設定の取得をサポート",
		"0.3.2-desc-15": "出力 HTTP 要求の送出時の「User-Agent」ヘッダーへのバージョン番号とプラットフォーム情報の組み込み",
		"0.3.2-desc-16": "Go 1.6 へのアップグレード",
		
		"0.3.3-desc-1": "CLI バージョン・チェックを有効化/無効化するために、「--check-version」オプションを「bluemix config」コマンドの下に追加",
		"0.3.3-desc-2": "「bluemix iam account-users」コマンドの出力にアカウント所有者を追加",
		"0.3.3-desc-3": "「bluemix scale」コマンドが、コンテナー・グループが組織の割り当て量を超えていないかチェック",
		"0.3.3-desc-4": "「bluemix route-map」コマンドのバインド済み経路で欠落しているホスト名を修正",
		"0.3.3-desc-5": "非推奨 API のリファクタリングとクリーン・アップ",
		
		repoTitle: "Bluemix CLI プラグイン・リポジトリー",
		bxPluginRepo: "Bluemix CLI プラグイン・リポジトリー",
		cfPlugins: "Cloud Foundry CLI プラグイン",
		bxPlugins: "Bluemix CLI プラグイン",
		company: "会社:",
		versionLower: "バージョン:",
		homepage: "ホーム・ページ",
		author: "作成者:",
		authors: "作成者:",
		platforms: "プラットフォーム:",
		
		"cf CLI plug-in for dev mode support of IBM runtimes (Liberty and Node.js)": "IBM ランタイム (Liberty および  Node.js) の開発モードのサポート用の CF CLI プラグイン",
		"CLI for active-deploy to help you update applications with no downtime. Works only for Cloud Foundry apps, not IBM Containers.": "アクティブ・デプロイ用の CLI です。アプリケーションを更新してもダウンタイムはありません。Cloud Foundry アプリの場合のみ機能します。IBM Containers では機能しません。",
		"The plug-ins are similar to ICE commands, with bootstrap to IBM Containers and various methods.": "プラグインは ICE コマンドと同様に、IBM Containers および各種のメソッドへのブートストラップを備えています。",
		"Bluemix Admin Console CLI": "Bluemix 管理コンソール CLI",
		"cf CLI plug-in for IBM VPN service": "サービスとして機能する VPN 用の cf CLI プラグイン",
		
		"Bluemix CLI plug-in for IBM VPN service": "IBM VPN サービス用の Bluemix CLI プラグイン",
		"Bluemix CLI plug-in for Auto-Scaling service": "Auto-Scaling サービス用の Bluemix CLI プラグイン",
		"Bluemix CLI plug-in for Catalog Management": "カタログ管理用の Bluemix CLI プラグイン",
		"Bluemix Network Security Group plug-in": "Bluemix ネットワーク・セキュリティー・グループ・プラグイン",
		"bx-active-deploy-plugin-description": "アクティブ・デプロイ用の Bluemix CLI プラグイン。cf アプリでのみ機能し、コンテナーではまだ機能しません。"
	
})

