from subprocess import* 
def performConfig(workingDir=None):
	call(['/usr/sbin/setsebool','-P','NetworkManager_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','aisexec_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','allow_aisexec_rw_tmpfs','off'])
	call(['/usr/sbin/setsebool','-P','allow_console_login','off'])
	call(['/usr/sbin/setsebool','-P','allow_cvs_read_shadow','off'])
	call(['/usr/sbin/setsebool','-P','allow_daemons_dump_core','off'])
	call(['/usr/sbin/setsebool','-P','allow_daemons_use_tty','off'])
	call(['/usr/sbin/setsebool','-P','allow_domain_fd_use','off'])
	call(['/usr/sbin/setsebool','-P','allow_execheap','off'])
	call(['/usr/sbin/setsebool','-P','allow_execmem','off'])
	call(['/usr/sbin/setsebool','-P','allow_execmod','off'])
	call(['/usr/sbin/setsebool','-P','allow_execstack','off'])
	call(['/usr/sbin/setsebool','-P','allow_ftpd_anon_write','off'])
	call(['/usr/sbin/setsebool','-P','allow_ftpd_full_access','off'])
	call(['/usr/sbin/setsebool','-P','allow_ftpd_use_cifs','off'])
	call(['/usr/sbin/setsebool','-P','allow_ftpd_use_nfs','off'])
	call(['/usr/sbin/setsebool','-P','allow_gpg_execstack','off'])
	call(['/usr/sbin/setsebool','-P','allow_gssd_read_tmp','off'])
	call(['/usr/sbin/setsebool','-P','allow_httpd_anon_write','off'])
	call(['/usr/sbin/setsebool','-P','allow_httpd_bugzilla_script_anon_write','off'])
	call(['/usr/sbin/setsebool','-P','allow_httpd_cvs_script_anon_write','off'])
	call(['/usr/sbin/setsebool','-P','allow_httpd_mod_auth_pam','off'])
	call(['/usr/sbin/setsebool','-P','allow_httpd_nagios_script_anon_write','off'])
	call(['/usr/sbin/setsebool','-P','allow_httpd_prewikka_script_anon_write','off'])
	call(['/usr/sbin/setsebool','-P','allow_httpd_squid_script_anon_write','off'])
	call(['/usr/sbin/setsebool','-P','allow_httpd_sys_script_anon_write','off'])
	call(['/usr/sbin/setsebool','-P','allow_java_execstack','off'])
	call(['/usr/sbin/setsebool','-P','allow_kerberos','off'])
	call(['/usr/sbin/setsebool','-P','allow_mount_anyfile','off'])
	call(['/usr/sbin/setsebool','-P','allow_mounton_anydir','off'])
	call(['/usr/sbin/setsebool','-P','allow_mplayer_execstack','off'])
	call(['/usr/sbin/setsebool','-P','allow_nfsd_anon_write','off'])
	call(['/usr/sbin/setsebool','-P','allow_polyinstantiation','off'])
	call(['/usr/sbin/setsebool','-P','allow_postfix_local_write_mail_spool','off'])
	call(['/usr/sbin/setsebool','-P','allow_ptrace','off'])
	call(['/usr/sbin/setsebool','-P','allow_rsync_anon_write','off'])
	call(['/usr/sbin/setsebool','-P','allow_saslauthd_read_shadow','off'])
	call(['/usr/sbin/setsebool','-P','allow_smbd_anon_write','off'])
	call(['/usr/sbin/setsebool','-P','allow_ssh_keysign','off'])
	call(['/usr/sbin/setsebool','-P','allow_tftp_anon_write','off'])
	call(['/usr/sbin/setsebool','-P','allow_unconfined_execmem_dyntrans','off'])
	call(['/usr/sbin/setsebool','-P','allow_unconfined_mmap_low','off'])
	call(['/usr/sbin/setsebool','-P','allow_unlabeled_packets','off'])
	call(['/usr/sbin/setsebool','-P','allow_user_mysql_connect','off'])
	call(['/usr/sbin/setsebool','-P','allow_write_xshm','off'])
	call(['/usr/sbin/setsebool','-P','allow_ypbind','off'])
	call(['/usr/sbin/setsebool','-P','allow_zebra_write_config','off'])
	call(['/usr/sbin/setsebool','-P','amanda_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','amavis_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','apmd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','arpwatch_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','auditd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','automount_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','avahi_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','bluetooth_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','canna_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','cardmgr_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','ccs_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','cdrecord_read_content','off'])
	call(['/usr/sbin/setsebool','-P','clamd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','clamscan_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','clogd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','clvmd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','comsat_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','cron_can_relabel','off'])
	call(['/usr/sbin/setsebool','-P','crond_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','cupsd_config_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','cupsd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','cupsd_lpd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','cvs_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','cyrus_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','dbskkd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','dccd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','dccifd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','dccm_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','dhcpc_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','dhcpd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','disable_evolution_trans','off'])
	call(['/usr/sbin/setsebool','-P','disable_games_trans','off'])
	call(['/usr/sbin/setsebool','-P','disable_mozilla_trans','off'])
	call(['/usr/sbin/setsebool','-P','disable_thunderbird_trans','off'])
	call(['/usr/sbin/setsebool','-P','dlm_controld_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','dnsmasq_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','dovecot_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','fcron_crond','off'])
	call(['/usr/sbin/setsebool','-P','fenced_can_network_connect','off'])
	call(['/usr/sbin/setsebool','-P','fenced_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','fetchmail_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','fingerd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','freshclam_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','fsdaemon_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','ftp_home_dir','off'])
	call(['/usr/sbin/setsebool','-P','ftpd_connect_db','off'])
	call(['/usr/sbin/setsebool','-P','ftpd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','ftpd_is_daemon','off'])
	call(['/usr/sbin/setsebool','-P','gfs_controld_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','global_ssp','off'])
	call(['/usr/sbin/setsebool','-P','gpm_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','groupd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','gssd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','hald_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','hotplug_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','howl_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','hplip_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','httpd_builtin_scripting','off'])
	call(['/usr/sbin/setsebool','-P','httpd_can_network_connect','off'])
	call(['/usr/sbin/setsebool','-P','httpd_can_network_connect_db','off'])
	call(['/usr/sbin/setsebool','-P','httpd_can_network_relay','off'])
	call(['/usr/sbin/setsebool','-P','httpd_can_sendmail','off'])
	call(['/usr/sbin/setsebool','-P','httpd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','httpd_enable_cgi','off'])
	call(['/usr/sbin/setsebool','-P','httpd_enable_ftp_server','off'])
	call(['/usr/sbin/setsebool','-P','httpd_enable_homedirs','off'])
	call(['/usr/sbin/setsebool','-P','httpd_read_user_content','off'])
	call(['/usr/sbin/setsebool','-P','httpd_rotatelogs_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','httpd_setrlimit','off'])
	call(['/usr/sbin/setsebool','-P','httpd_ssi_exec','off'])
	call(['/usr/sbin/setsebool','-P','httpd_suexec_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','httpd_tty_comm','off'])
	call(['/usr/sbin/setsebool','-P','httpd_unified','off'])
	call(['/usr/sbin/setsebool','-P','httpd_use_cifs','off'])
	call(['/usr/sbin/setsebool','-P','httpd_use_nfs','off'])
	call(['/usr/sbin/setsebool','-P','inetd_child_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','inetd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','innd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','ipsec_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','irqbalance_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','iscsid_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','kadmind_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','klogd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','kpropd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','krb5kdc_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','ktalkd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','lpd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','mail_read_content','off'])
	call(['/usr/sbin/setsebool','-P','mailman_mail_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','mdadm_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','mozilla_read_content','off'])
	call(['/usr/sbin/setsebool','-P','mysqld_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','nagios_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','named_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','named_write_master_zones','off'])
	call(['/usr/sbin/setsebool','-P','nfs_export_all_ro','off'])
	call(['/usr/sbin/setsebool','-P','nfs_export_all_rw','off'])
	call(['/usr/sbin/setsebool','-P','nfsd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','nmbd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','nrpe_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','nscd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','ntpd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','oddjob_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','oddjob_mkhomedir_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','openvpn_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','openvpn_enable_homedirs','off'])
	call(['/usr/sbin/setsebool','-P','pcscd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','pegasus_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','piranha_fos_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','piranha_lvs_can_network_connect','off'])
	call(['/usr/sbin/setsebool','-P','piranha_lvs_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','piranha_pulse_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','piranha_web_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','portmap_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','postfix_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','postgresql_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','postgrey_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','pppd_can_insmod','off'])
	call(['/usr/sbin/setsebool','-P','pppd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','pppd_for_user','off'])
	call(['/usr/sbin/setsebool','-P','pptp_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','prelude_audisp_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','prelude_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','prelude_lml_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','privoxy_connect_any','off'])
	call(['/usr/sbin/setsebool','-P','privoxy_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','ptal_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','pyzord_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','qdiskd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','qemu_full_network','off'])
	call(['/usr/sbin/setsebool','-P','qemu_use_cifs','off'])
	call(['/usr/sbin/setsebool','-P','qemu_use_comm','off'])
	call(['/usr/sbin/setsebool','-P','qemu_use_nfs','off'])
	call(['/usr/sbin/setsebool','-P','qemu_use_usb','off'])
	call(['/usr/sbin/setsebool','-P','racoon_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','racoon_read_shadow','off'])
	call(['/usr/sbin/setsebool','-P','radiusd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','radvd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','rdisc_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','read_default_t','off'])
	call(['/usr/sbin/setsebool','-P','read_untrusted_content','off'])
	call(['/usr/sbin/setsebool','-P','readahead_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','regex_milter_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','restorecond_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','rgmanager_can_network_connect','off'])
	call(['/usr/sbin/setsebool','-P','rgmanager_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','rhgb_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','ricci_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','ricci_modclusterd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','rlogind_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','rpcd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','rshd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','rsync_client','off'])
	call(['/usr/sbin/setsebool','-P','rsync_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','rsync_export_all_ro','off'])
	call(['/usr/sbin/setsebool','-P','run_ssh_inetd','off'])
	call(['/usr/sbin/setsebool','-P','samba_domain_controller','off'])
	call(['/usr/sbin/setsebool','-P','samba_enable_home_dirs','off'])
	call(['/usr/sbin/setsebool','-P','samba_export_all_ro','off'])
	call(['/usr/sbin/setsebool','-P','samba_export_all_rw','off'])
	call(['/usr/sbin/setsebool','-P','samba_share_fusefs','off'])
	call(['/usr/sbin/setsebool','-P','samba_share_nfs','off'])
	call(['/usr/sbin/setsebool','-P','saslauthd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','secure_mode_insmod','off'])
	call(['/usr/sbin/setsebool','-P','secure_mode_policyload','off'])
	call(['/usr/sbin/setsebool','-P','setrans_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','setroubleshootd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','slapd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','smbd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','snmpd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','spamass_milter_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','spamassassin_can_network','off'])
	call(['/usr/sbin/setsebool','-P','spamd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','spamd_enable_home_dirs','off'])
	call(['/usr/sbin/setsebool','-P','squid_connect_any','off'])
	call(['/usr/sbin/setsebool','-P','squid_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','ssh_sysadm_login','off'])
	call(['/usr/sbin/setsebool','-P','staff_read_sysadm_file','off'])
	call(['/usr/sbin/setsebool','-P','stunnel_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','stunnel_is_daemon','off'])
	call(['/usr/sbin/setsebool','-P','swat_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','syslogd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','tcpd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','telnetd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','tftpd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','tzdata_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','udev_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','use_lpd_server','off'])
	call(['/usr/sbin/setsebool','-P','use_nfs_home_dirs','off'])
	call(['/usr/sbin/setsebool','-P','use_samba_home_dirs','off'])
	call(['/usr/sbin/setsebool','-P','user_direct_mouse','off'])
	call(['/usr/sbin/setsebool','-P','user_dmesg','off'])
	call(['/usr/sbin/setsebool','-P','user_net_control','off'])
	call(['/usr/sbin/setsebool','-P','user_ping','off'])
	call(['/usr/sbin/setsebool','-P','user_rw_noexattrfile','off'])
	call(['/usr/sbin/setsebool','-P','user_tcp_server','off'])
	call(['/usr/sbin/setsebool','-P','user_ttyfile_stat','off'])
	call(['/usr/sbin/setsebool','-P','uucpd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','vhostmd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','virt_use_comm','off'])
	call(['/usr/sbin/setsebool','-P','virt_use_fusefs','off'])
	call(['/usr/sbin/setsebool','-P','virt_use_nfs','off'])
	call(['/usr/sbin/setsebool','-P','virt_use_samba','off'])
	call(['/usr/sbin/setsebool','-P','virt_use_sysfs','off'])
	call(['/usr/sbin/setsebool','-P','virt_use_usb','off'])
	call(['/usr/sbin/setsebool','-P','virtd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','winbind_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','write_untrusted_content','off'])
	call(['/usr/sbin/setsebool','-P','xdm_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','xdm_sysadm_login','off'])
	call(['/usr/sbin/setsebool','-P','xend_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','xfs_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','xm_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','ypbind_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','yppasswdd_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','ypserv_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','ypxfr_disable_trans','off'])
	call(['/usr/sbin/setsebool','-P','zebra_disable_trans','off'])
if __name__ == '__main__':
	performConfig()